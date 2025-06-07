FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

user_input = int(input("Enter the temperature to convert: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")


def convert_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f'{fahrenheit}°F is {C}°F')
    

def convert_to_fahrenheit(celsius):
    F = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f'{celsius}°C is {F}°F')

if temp_type == "C":
    convert_to_fahrenheit(user_input)
elif temp_type == "F":
    convert_to_celsius(user_input)
else:
    print("Invalid temperature. Please enter a numeric value.")

