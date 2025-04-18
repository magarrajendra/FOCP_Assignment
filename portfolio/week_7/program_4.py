""" One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes."""

def letter_frequency(msg):
    msg = msg.lower()

    letter_counts = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}

    for char in msg:
        if char.isalpha():
            letter_counts[char] += 1

    most_common_letters = sorted(letter_counts, key=letter_counts.get, reverse=True)[:6]

    print("Six most common letters and their counts:")
    for char in most_common_letters:
        count = letter_counts[char]
        print(f"{char}: {count}")

if __name__ == "__main__":
    message = "Martinez, Mr John Wick is here and he has brought a surprise gift for you!"
    letter_frequency(message)
