phone_number= input('Phone number: ')
separated_phone_number = f'{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}'
print(f'The separated phone number is: {separated_phone_number}')