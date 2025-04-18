""" Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in Fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae). """

def centigrade_to_fahrenheit(centigrade):
    return (centigrade * 9 / 5) + 32

def fahrenheit_to_centigrade(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius_temperature = 25.0
fahrenheit_temperature = centigrade_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature}°C = {fahrenheit_temperature}°F")

fahrenheit_temperature = 77.0
celsius_temperature = fahrenheit_to_centigrade(fahrenheit_temperature)
print(f"{fahrenheit_temperature}°F = {celsius_temperature}°C")
