###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = (total-north)
print("World population: ", total)
print("Number of people living in the Northern Hemisphere:", north)
print("Number of people living in the Southern Hemisphere:", south)
print("Percentage of the total population living in the Northern Hemisphere: ", north/total*100)
print("Percentage of the total population living in the Southern Hemisphere: ", south/total*100)