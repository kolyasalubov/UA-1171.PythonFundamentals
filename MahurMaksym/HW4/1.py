celsius = float(input("Enter temperature in Celsius: "))

if celsius < -273.15:
    print("Temperature below absolute zero is not possible.")
else:
    fahrenheit = (celsius * 9/5) + 32

    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")