###
#Program that checks whether the vehicle speed entered from 
# the keyboard is between 40 and 140 km/h
#
vehicle_speed = int(input('Enter the speed of the vehicle: '))
valid_speed = vehicle_speed >=40 and vehicle_speed <= 140
print(f'Speed is valid: {valid_speed}')
