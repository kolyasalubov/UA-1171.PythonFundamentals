c = int(input('Celsius: '))
if -273.15 > c:
    print('Temperature below absolute zero (-273.15°C)')
else:
    f = (c * 9 / 5) + 32
    print(f'{c}°C - {f}°F')