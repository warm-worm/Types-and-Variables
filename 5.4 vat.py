###
#program that tells you the amount from the vat input
#
amount = float(input('Amount before Vat: '))
vat = float(amount*0.23)
rounded_vat = round(vat , 2)
print(f'The Vat from the amount of {amount} equals approximately {rounded_vat}.')
