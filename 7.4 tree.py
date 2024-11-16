###
#Program that, based on the circumference of the tree entered 
# from the keyboard, calculates and prints the value True if 
# the tree can be cut down, or print the value False otherwise
#
import math
circumference = float(input('Enter the tree circumference in cm: '))
diameter = circumference / math.pi
can_cut = diameter >= 50
print(f'The tree can be cut down: {can_cut}')
