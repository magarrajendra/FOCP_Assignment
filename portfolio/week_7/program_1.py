""" Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's']."""

def unique_letters(string):
    string = string.lower()
    unique_set = set(char for char in string if char.isalpha())
    sorted_list = sorted(unique_set)
    return sorted_list

if __name__ == "__main__":
    input_string = "cheese"
    result = unique_letters(input_string)
    print(result)
