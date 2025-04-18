""" Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way."""

def simple_encrypt(message):
    message_without_spaces = message.replace(" ", "")
    encrypted_message = message_without_spaces[::-1]
    return encrypted_message

if __name__ == "__main__":
    original_message = "Noo, Mr. John Wick is here!!!"
    encrypted_result = simple_encrypt(original_message)
    print(f"Original Message: {original_message}")
    print(f"Encrypted Message: {encrypted_result}")
