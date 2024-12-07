import sys

COMMANDS = ['exit', 'echo']

def main():

    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    splitted_command = command.split()
    if splitted_command[0] not in COMMANDS:
        print(f"{splitted_command[0]}: command not found")
        main()
    elif splitted_command[0] == "exit" and splitted_command[1] == "0":
        exit(0)
    elif splitted_command[0] == "echo":
        print(" ".join(splitted_command[1:]))
        main()

if __name__ == "__main__":
    main()
