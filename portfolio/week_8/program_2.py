""" 2. The Unix diff command compares two files and reports the differences, if any.
Write a simple implementation of this that takes two file names as command-line
arguments and reports whether the two files are the same. (Define "same" as
having the same contents.) """

import sys

def diff(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()

            if content1 == content2:
                print("Files are the same.")
            else:
                print("Files are different.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <file1> <file2>")
    else:
        diff(sys.argv[1], sys.argv[2])
