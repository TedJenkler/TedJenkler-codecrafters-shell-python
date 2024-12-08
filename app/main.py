import sys
import os
import subprocess

COMMANDS = ['exit', 'echo', 'type']

path_variable = os.environ.get("PATH")

path_list = path_variable.split(':')

def main():

    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    splitted_command = command.split()
    if "_" in splitted_command[0] and len(splitted_command) == 2:
        subprocess.run([splitted_command[0], splitted_command[1]])
        main()
    elif splitted_command[0] not in COMMANDS:
        print(f"{splitted_command[0]}: command not found")
        main()
    elif splitted_command[0] == "exit" and splitted_command[1] == "0":
        exit(0)
    elif splitted_command[0] == "echo":
        print(" ".join(splitted_command[1:]))
        main()
    elif splitted_command[0] == "type":
        if splitted_command[1] in COMMANDS:
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
