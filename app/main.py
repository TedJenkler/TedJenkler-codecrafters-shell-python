import sys
import os
import subprocess

COMMANDS = ['exit', 'echo', 'type', 'pwd', 'cd', 'cat']

path_variable = os.environ.get("PATH")

path_list = path_variable.split(':')

def main():

    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    splitted_command = command.split()
    if "_" in splitted_command[0] and len(splitted_command) == 2:
        subprocess.run([splitted_command[0], splitted_command[1]])
    elif splitted_command[0] not in COMMANDS:
        print(f"{splitted_command[0]}: command not found")
    elif splitted_command[0] == "cat":
        splitted = command[4:].split("' '")
        clean = []
        result = []
        for path in splitted:
            x = path.split("f")
            clean.append(x[0].lstrip("'"))
            clean.append(f"f{x[1]}".rstrip("'"))
        for i in range(0, len(clean) - 1, 2):
            directory = clean[i]
            target_file = clean[i + 1]
            for root, dirs, files in os.walk(directory):
                if target_file in files:
                    file_path = os.path.join(root, target_file)
                    with open(file_path, 'r') as file:
                        content = file.read()
                        result.append(content)
                    break
        print("".join(result).strip())
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
        if "'" in command[5]:
            print(command[5:].strip("'"))
        else:
            print(" ".join(splitted_command[1:]))
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
