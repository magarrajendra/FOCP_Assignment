""" Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long """

new_password = input("Enter your new password: ")

if not 8 <= len(new_password) <= 12:
    print("Error! password must be between 8 and 12 characters.")
else:
    confirm_password = input("Confirm your new password: ")

    if new_password == confirm_password:
        print("Password Set!")
    else:
        print("Error! Passwords do not match.")
