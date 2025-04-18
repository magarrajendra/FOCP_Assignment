""" Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program. """

def count_upper_lower(string):
    """Counts the number of uppercase and lowercase letters in a string."""
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


if __name__ == "__main__":
    test_string = "Hello, Mr. John Wick. Welcome to Nepal."
    upper, lower = count_upper_lower(test_string)

    print(f"Original string: {test_string}")
    print(f"Number of uppercase letters: {upper}")
    print(f"Number of lowercase letters: {lower}")


