""" Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise, it should print
a greeting with their name as before. """

get_name = input("Hello, What is your name? ")
if get_name:
    print(f"Hello, {get_name}. Good to meet you!")
else:
    print(f"Hello, Stranger!")
