celsius = int(input('enter the temperature in celsius: '))

if celsius > -273.15:
    farenheit = (celsius * 9/5) + 32
    print(str(celsius) + "°C is equivalent to", str(round(farenheit)) +"°F")
else:
    print('error: temperature below absolute zero') 