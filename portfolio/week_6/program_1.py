""" Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think! """

def int_to_binary(num):
    if num > 0:
        binary_representation = bin(num)
        return binary_representation[2:]
    else:
        raise ValueError("Input must be a positive integer")


if __name__ == "__main__":
    try:
        positive_integer = int(input("Enter any positive integer for binary conversion: "))
        result = int_to_binary(positive_integer)
        print(f"Binary representation of {positive_integer} is: {result}")
    except ValueError as e:
        print(e)
