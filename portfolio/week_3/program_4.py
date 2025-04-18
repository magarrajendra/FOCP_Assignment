""" Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'] """

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
new_password = input("Enter your new password: ")

if new_password.lower() in BAD_PASSWORDS:
    print("Error! Entered password is commonly used. Try new password.")
elif not 8 <= len(new_password) <= 12:
    print("Error! Password must be between 8 and 12 characters.")
else:
    confirm_password = input("Confirm your new password: ")

    if new_password == confirm_password:
        print("Password Set!")
    else:
        print("Error! Passwords do not match.")
