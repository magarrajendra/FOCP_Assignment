""" The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for dry runs or white-box
testing). Write an implementation of this command. It should take the name of the
files as a command-line argument."""

import sys

def nl(filename):
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, start=1):
                print(f"{i:>6}\t{line.rstrip()}")
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl.py <filename>")
    else:
        nl(sys.argv[1])
