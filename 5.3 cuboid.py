###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
volume = a * b * c
area = 2*( a * b + a * c + b * c)
print (f'Volume of the cuboid equals {volume}.')
print (f'Surface area of the cuboid equals {area}.')
