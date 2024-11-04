###
# A program that prints your height both in cm and in feet and inches.
#
cm = int(input('Enter your height: '))
feet = cm*0.0328
inches = cm*0.3937
# calculate the number of feet
rounded_feet = round(feet , 1)
rounded_inches = round(inches , 1)
print(f'I am {cm}cm tall, i.e. {rounded_feet} feet and {rounded_inches} inches.')