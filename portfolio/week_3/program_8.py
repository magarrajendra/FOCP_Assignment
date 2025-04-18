""" Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times" """

number = int(input("Enter number between 0 and 12 to generate it's times table: "))

if not 0 <= abs(number) <= 12:
    print("Invalid input! Please enter a number between 0 and 12.")
elif number > 0:
    print(f"Generating the times table for: {number}")
    for i in range(13):
        result = i * number
        print(f"{i} * {number} = {result}")
else:
    backward_number = abs(number)
    print(f"Generating the times table backwards for: {-backward_number}")

    for i in range(12, -1, -1):
        print(f"{-backward_number} x {i} = {-backward_number * i}")
