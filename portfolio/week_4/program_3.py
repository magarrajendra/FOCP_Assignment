""" Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur. """

get_name = input("Hello, What is your name? ")

if get_name:
    formatted_name = get_name.title()
    print(f"Hello, {formatted_name}. Good to meet you!")
else:
    print(f"Hello, Stranger!")
