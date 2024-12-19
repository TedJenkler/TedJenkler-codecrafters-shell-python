import sys
import os
import subprocess
import re
import shlex

COMMANDS = ['exit', 'echo', 'type', 'pwd', 'cd', 'cat', 'exe']

path_variable = os.environ.get("PATH")

path_list = path_variable.split(':')

def cat(splitted):
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

def main():

    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    splitted_command = command.split()
    splitted_command[0] = splitted_command[0].strip("'").strip('"')
    if "_" in splitted_command[0] and len(splitted_command) == 2:
        subprocess.run([splitted_command[0], splitted_command[1]])
    elif splitted_command[0] not in COMMANDS:
        print(f"{splitted_command[0]}: command not found")
    elif splitted_command[0] == "exe":
        splitted = splitted_command[-1]
        try:
            with open(splitted, 'r') as file:
                contents = file.read()
                print("".join(contents).strip())
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif splitted_command[0] == "cat":
        splitted = shlex.split(command[4:])
        cat(splitted)
    elif splitted_command[0] == "pwd":
        current_path = os.getcwd()
        print(current_path)
    elif splitted_command[0] == "cd":
        new_path = splitted_command[1]
        if new_path == '~':
            home_directory = os.environ.get('HOME')
            os.chdir(home_directory)
        elif os.path.isdir(new_path):
            os.chdir(new_path)
        else:
            print(f"cd: {new_path}: No such file or directory")
    elif splitted_command[0] == "exit" and splitted_command[1] == "0":
        exit(0)
    elif splitted_command[0] == "echo":
        x = shlex.split(command, posix=True)
        print(" ".join(x[1:]))
    elif splitted_command[0] == "type":
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

    main()

if __name__ == "__main__":
    main()
