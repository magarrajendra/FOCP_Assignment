""" Write a program that takes a centigrade temperature and displays the equivalent in
Fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format."""

def centigrade_to_fahrenheit(centigrade):
    """Converts temperature from Centigrade (Celsius) to Fahrenheit."""
    return (centigrade * 9 / 5) + 32

def main():
    temperature_input = input("Enter temperature in Centigrade (e.g., 25C): ")
    if temperature_input[-1].upper() == 'C':
        try:
            centigrade = float(temperature_input[:-1])  # Removing the 'C' and converting to float
            fahrenheit = centigrade_to_fahrenheit(centigrade)
            print(f"{centigrade}C = {fahrenheit:.2f}F")
        except ValueError:
            print("Invalid input. Please enter a valid number followed by 'C'.")
    else:
        print("Invalid format. Input must end with 'C'.")

if __name__ == "__main__":
    main()
