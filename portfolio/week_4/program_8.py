""" Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value. """

def centigrade_to_fahrenheit(centigrade):
    """Converts temperature from Centigrade (Celsius) to Fahrenheit."""
    return (centigrade * 9 / 5) + 32

def calculate_mean(temps: list):
    """Calculates the mean of a list of numbers."""
    return sum(temps) / len(temps)

def main():
    temperatures = []
    while True:
        temp_input = input("Enter temperature in Centigrade (e.g., 25C), or press Enter to finish: ")
        if temp_input == "":
            break
        if temp_input[-1].upper() == 'C':
            try:
                centigrade = float(temp_input[:-1])
                temperatures.append(centigrade)
            except ValueError:
                print("Invalid input. Please enter a valid number followed by 'C'.")
        else:
            print("Invalid format. Input must end with 'C'.")

    if temperatures:
        print("\nTemperature Statistics:")
        print(f"Maximum: {max(temperatures):.2f}°C")
        print(f"Minimum: {min(temperatures):.2f}°C")
        print(f"Mean:    {calculate_mean(temperatures):.2f}°C")

if __name__ == "__main__":
    main()
