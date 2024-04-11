temperature_in_celsius = float(input('Enter the Temperature in Celsius: '))

if temperature_in_celsius == -273.15:
    print(f'Error. The Temperature {temperature_in_celsius}°C is equal to '
          f'Absolute zero (-273.15°C).')
elif temperature_in_celsius < -273.15:
    print(f'Error. The Temperature {temperature_in_celsius}°C is less than '
          f'Absolute zero (-273.15°C).')
else:
    temperature_in_fahrenheit = temperature_in_celsius * 9 / 5 + 32
    print(f'{temperature_in_celsius}°C is equivalent to {temperature_in_fahrenheit}°F.')
