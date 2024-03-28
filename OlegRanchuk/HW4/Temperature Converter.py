user_temp = float(input('Enter yout temperature:'))

Faren = (user_temp * 9 / 5) + 32
if user_temp < -273.15:
    print('Error temperature below absolute zero is not possible')
else:
    print (f'{user_temp} °C is equivalent to {Faren} °F')
