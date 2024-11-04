###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
distance = last_letter_code - first_letter_code
if distance > 2:
    number_of_letters = distance - 1
    print(f'Between {first} and {last} there are {number_of_letters} letters.')
elif distance == 2:
    number_of_letters = distance    
    print(f'There is 1 letter between {first} and {last}.')
elif distance >= 1:
    print(f'There are 0 letters between {first} and {last}.')
elif distance == 0:
    print(f'There are 0 letters between {first} and {last}.')
