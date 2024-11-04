###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone_number= input('Enter phone number: ')
separated_phone_number = f'{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}'
print(f'The separated phone number is: {separated_phone_number}')