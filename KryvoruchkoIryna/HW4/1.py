temp_cels = float(input("Enter temperature in Celsius: "))

if temp_cels >= -273.15:
    temp_far = (temp_cels * 9 / 5 + 32)
    print(f"{temp_cels}°C is equivalent to {temp_far}°F")
else:
    print("Error: Temperature below absolute zero (-273.15°C)")