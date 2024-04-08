celsius = float(input("Enter a temperature in Celsius "))

if celsius < -273.15:
    print("Temperatures below 273.15C are not allowed")
else: fahrenheit = float((celsius * 9/5) + 32)
print(f"Temperatures in Farenheit {fahrenheit}°F")    