###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
celsius = int(input('Enter the temperature in Celsius: '))
kelvin = celsius + 273.15
fahrenheit = celsius*(9/5)+32
print(f'The temperature of {celsius}°C is {fahrenheit}°F and {kelvin}K.')
