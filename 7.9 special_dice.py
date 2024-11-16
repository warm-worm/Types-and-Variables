###
# Program that prints the number of dice rolled and 
# the value True if the number rolled is 1 or 6
#
import random
dice_roll = random.randint(1,6)
special_value = dice_roll == 1 or dice_roll == 6
print(f'Special value (1 or 6) of {dice_roll}: {special_value}')
