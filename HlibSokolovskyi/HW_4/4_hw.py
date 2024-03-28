temp_in_C = float(input("Enter the temperature in Celsius: "))
if temp_in_C < -273.15:
    print("Error: Temperature is below absolute zero (-273.15⁰C)")
else:
    temp_in_F = round(((temp_in_C*9/5) + 32), 2)
    print(f"{temp_in_C}⁰C is eqivalent to {temp_in_F}⁰F.")

