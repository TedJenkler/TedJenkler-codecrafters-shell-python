# Build Your Own Shell - Python Implementation

This repository contains a Python implementation of a POSIX-compliant shell, built as part of the **"Build Your Own Shell"** challenge. The shell can interpret and execute a variety of commands, both built-in and external, and provides a basic REPL (Read-Eval-Print Loop) interface.

## Features

- **Built-in commands**:
  - `cd`: Change the current directory
  - `pwd`: Print the current working directory
  - `echo`: Print text to the terminal
  - `cat`: Display the contents of a file
  - `exe`: Execute a file by reading and printing its contents
  - `type`: Show whether a command is a built-in or external command
  - `exit`: Exit the shell
  
- **Support for external commands**: You can run executable commands if they are available in your system's `PATH`.

## Requirements

- Python 3.11 or higher

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/build-your-own-shell.git
   cd build-your-own-shell
