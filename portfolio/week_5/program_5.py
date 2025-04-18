""" Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!"""

def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def process_temperatures(celsius_temperatures):
    if not celsius_temperatures:
        print("No temperatures entered.")
        return

    fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in celsius_temperatures]

    max_temp = max(fahrenheit_temperatures)
    min_temp = min(fahrenheit_temperatures)
    mean_temp = sum(fahrenheit_temperatures) / len(fahrenheit_temperatures)

    print(f"Maximum temperature: {max_temp:.2f} F")
    print(f"Minimum temperature: {min_temp:.2f} F")
    print(f"Mean temperature: {mean_temp:.2f} F")