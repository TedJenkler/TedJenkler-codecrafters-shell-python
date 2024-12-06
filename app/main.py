import sys

COMMANDS = []

def main():

    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    if command not in COMMANDS:
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
