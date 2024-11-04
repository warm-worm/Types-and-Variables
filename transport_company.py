###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter (in dollars): '))
fuel_consumption = float(input('Enter the fuel consumption in liters per 100 km: '))
total_fuel_consumption = distance*(fuel_consumption*0.01)
rouded_total_fuel_consumption = round(total_fuel_consumption , 2)
total_cost = total_fuel_consumption*fuel_price
rounded_total_cost = round(total_cost , 2)
print(f'The total fuel consumption equals: {rouded_total_fuel_consumption} l')
print(f'The total cost of transporting goods is: {rounded_total_cost} $')