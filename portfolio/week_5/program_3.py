""" Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them. """

import sys

def find_shortest(arguments):
    sorted_arguments = sorted(arguments, key=len)

    shortest = sorted_arguments[0]

    return shortest

if __name__ == "__main__":
    cmd_line_args = sys.argv[1:]

    if not cmd_line_args:
        print("No arguments provided. Please provide at least one argument.")
    else:
        shortest_argument = find_shortest(cmd_line_args)
        print("Shortest argument:", shortest_argument)