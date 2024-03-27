Temperature_Celsius = float(input("enter a temperature in celsius: "))

def convers_to_fahrenheit(Temperature_Celsius):
    return (Temperature_Celsius*9/5)+32

if Temperature_Celsius<-273.15:
    print("Error: Temperature below absolute zero(-273.15°C)")
else:
    print(f'{Temperature_Celsius}°C is equilent to {convers_to_fahrenheit(Temperature_Celsius)}°F')