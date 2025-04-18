""" Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function. """

def is_valid_integer(num):
    return 0 <= num <= 100

def main():
    test_values = [-10, 0, 50, 100, 101]
    for i in test_values:
        result = is_valid_integer(i)
        print(f"{i} is in the range 0 to 100: {result}")

if __name__ == "__main__":
    main()

