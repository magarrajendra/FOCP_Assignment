""" When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.) """

def remove_last_character(input_string):
    if len(input_string) <= 2:
        return input_string
    else:
        return input_string[:-1]

if __name__ == "__main__" :
    msg_1 = "Mr. John Wick.\n"
    msg_2 = "Mr. John Wick."
    msg_3 = "No"

    modified_msg_1 = remove_last_character(msg_1)
    modified_msg_2 = remove_last_character(msg_2)
    modified_msg_3 = remove_last_character(msg_3)

    print(f"Original text:{msg_1}Modified text:{modified_msg_1}\n\n"
          f"Original text:{msg_2}\nModified text:{modified_msg_2}\n\n"
          f"Original text:{msg_3}\nModified text:{modified_msg_3}")


