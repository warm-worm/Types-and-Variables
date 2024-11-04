###
#The price of the product on the price tag is given before 
# and after the discount is applied. 
# Write a program that allows you to enter the product price and discount. 
# Print the product price, discount, discounted product price, 
# and the difference between the product price before and after the discount. 
# Print all prices with two decimal places
#
price = float(input('Enter price: '))
discount_percentage = float(input('Enter the discount percentage: '))
discount = discount_percentage*0.01
discounted_price = float(round(price*discount , 2))
rounded_price = round(price , 2)
rounded_discount = round(discount , 2)
difference = float(price-discounted_price)
rounded_difference = round(difference , 2)
print(f'The product price of {price} with the discount of {discount} equals approximately {discounted_price}.')
print(f'The difference between the product price before and after the discount equals approximately {rounded_difference}.')