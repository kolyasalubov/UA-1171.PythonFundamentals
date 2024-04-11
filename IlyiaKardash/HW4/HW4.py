LOWEST_TEMP = float(-273.15)

celsius_in = float(input("Enter a temperature in Celsius: "))

if celsius_in != LOWEST_TEMP:
    print((celsius_in * 9/5) + 32, u"\u00b0","F")
else:
    print("Error.Can't be converted. Try another number")
