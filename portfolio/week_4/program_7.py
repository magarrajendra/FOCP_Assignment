""" Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean. """

def centigrade_to_fahrenheit(centigrade):
    return (centigrade * 9 / 5) + 32

def calculate_mean(temps: list):
    return sum(temps) / len(temps)

def main():
    temperatures = []
    for i in range(6):
        temp_input = input(f"Enter temperature {i + 1} in Centigrade (e.g., 25C): ")
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

