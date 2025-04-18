""" Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument)."""

import sys

def report_arguments_count():
    arguments_count = len(sys.argv) - 1
    print(f"Number of command-line arguments provided: {arguments_count}")

if __name__ == "__main__":
    report_arguments_count()
