import math
height = float(input("Enter the height of the observer in meters: "))
distance = 3.57 * (height ** 0.5)
print ("The distance to the horizon from the distance of", height, "meters is (approximately):", round(distance, 2), "km")
