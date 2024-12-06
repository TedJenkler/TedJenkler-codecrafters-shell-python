import sys

COMMANDS = ['exit 0']

def main():

    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    if command not in COMMANDS:
        print(f"{command}: command not found")
        main()
    elif command == "exit 0":
        exit(0)

if __name__ == "__main__":
    main()
