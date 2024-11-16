###
# Calculation of circle area and circumference 
#
import math
radius = int(input('Enter the radius: '))
# determine radius and PI values
area = math.pi*(radius**2)
rounded_area = round(area , 2)
# calculate area 
diameter = radius*2
circumference = 2*(math.pi * radius)
rounded_circumference = round(circumference , 2)
# calculate circumference 
print(f'Circle with a radius of {radius} has the area of approximately {rounded_area} and circumference of approximately {rounded_circumference}.')
# print results
