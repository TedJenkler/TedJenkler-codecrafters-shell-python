import sys
import os
import subprocess
import re
import shlex

COMMANDS = {
    'exit': 'exit_command',
    'echo': 'echo_command',
    'type': 'type_command',
    'pwd': 'pwd_command',
    'cd': 'cd_command',
    'cat': 'cat_command',
    'exe': 'exe_command'
}

path_variable = os.environ.get("PATH")
path_list = path_variable.split(':')

def read_file(file_path):
    """ Helper function to read the contents of a file safely. """
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

def cat_command(splitted, command):
    """
    This function handles the 'cat' command. It attempts to read files from
    the specified directories and prints their contents if they exist.
    """
    splitted = shlex.split(command[4:])
    result = []
    for path in splitted:
        directory, target_file = os.path.split(path)
        
        if not directory or not target_file:
            print(f"Invalid path: '{path}'")
            continue

        if not os.path.isdir(directory):
            print(f"Directory '{directory}' does not exist.")
            continue
        
        found = False
        for root, dirs, files in os.walk(directory):
            if target_file in files:
                file_path = os.path.join(root, target_file)
                with open(file_path, 'r') as file:
                    content = file.read()
                result.append(content)
                found = True
                break
        
        if not found:
            print(f"File '{target_file}' not found in directory '{directory}'")

    if result:
        print("".join(result).strip())
    else:
        print("No files were found.")

def exe_command(splitted_command, command):
    """ Handles the 'exe' command. Reads the contents of the specified file. """
    file_path = splitted_command[-1]
    content = read_file(file_path)
    print(content)

def pwd_command(splitted_command, command):
    """
    This function handles the 'pwd' command. It prints the current working directory.
    """
    current_path = os.getcwd()
    print(current_path)

def cd_command(splitted_command, command):
    """
    This function handles the 'cd' command. It attempts to change the current
    directory to the specified path.
    """
    new_path = splitted_command[1]
    if new_path == '~':
        home_directory = os.environ.get('HOME')
        os.chdir(home_directory)
    elif os.path.isdir(new_path):
        os.chdir(new_path)
    else:
        print(f"cd: {new_path}: No such file or directory")

def echo_command(splitted_command, command):
    """
    This function handles the 'echo' command. It splits the command and prints
    the arguments passed to echo.
    """
    x = shlex.split(command, posix=True)
    print(" ".join(x[1:]))

def type_command(splitted_command, command):
    """
    This function handles the 'type' command. It checks whether the specified
    command is a shell builtin or a file and prints the corresponding message.
    """
    if splitted_command[1] in COMMANDS:
        if splitted_command[1] == "cat":
            print("cat is /bin/cat")
        else:
            print(f"{splitted_command[1]} is a shell builtin")
    else:
        for directory in path_list:
            potential_path = os.path.join(directory, splitted_command[1])
            if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                print(potential_path)
                main()
        print(f"{splitted_command[1]}: not found")

def exit_command(splitted_command, command):
    """
    This function handles the 'exit' command and exits the program if the argument is '0'.
    """
    if len(splitted_command) == 2 and splitted_command[1] == "0":
        exit(0)

def main():

    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    splitted_command = command.split()
    splitted_command[0] = splitted_command[0].strip("'").strip('"')

    if "_" in splitted_command[0] and len(splitted_command) == 2:
        # Execute a subprocess if the command is a valid executable
        subprocess.run([splitted_command[0], splitted_command[1]])
    elif splitted_command[0] in COMMANDS:
        globals()[COMMANDS[splitted_command[0]]](splitted_command, command)
    else:
        print(f"{splitted_command[0]}: command not found")
    
    main()

if __name__ == "__main__":
    main()
