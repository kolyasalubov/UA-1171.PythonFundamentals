temperature_in_celsius = int(input("Enter the temperature in Celsius: "))
temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32
if (temperature_in_celsius < -273.15):
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    print(f"{temperature_in_celsius} is equal to "
      f"{temperature_in_fahrenheit}")