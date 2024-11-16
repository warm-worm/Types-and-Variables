###
#Program that reads an integer number from the keyboard 
# and prints that value as a binary and hexadecimal number
#
integer = int(input('Enter an integer number: '))
binary = bin(integer)
hexadecimal = hex(integer)
print(f'Binary number: {binary}')
print(f'Hexadecimal number: {hexadecimal}')
