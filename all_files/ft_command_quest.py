"""
Data Quest - Exercise 0: Command Quest
This module demonstrates command-line argument handling using sys.argv.
Learn to receive external data through command-line arguments and display
them in a user-friendly format.

Functions:
    main: Process and display command-line arguments

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-05)
"""

import sys


def main():
    args = sys.argv
    program_name = args[0]
    user_args = args[1:]
    total_args = len(args)
    num_user_args = len(user_args)

    print("=== Command Quest ===")

    if num_user_args == 0:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {num_user_args}")
        for i, arg in enumerate(user_args, start=1):
            print(f"Argument {i}: {arg}")
        print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
