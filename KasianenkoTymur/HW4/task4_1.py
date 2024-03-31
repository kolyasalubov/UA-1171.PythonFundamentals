answer='yes'
while answer=='yes' or answer=='y':

    Celsius = input('Enter the temperature in Celsius:')
    if float(Celsius)>-273.15:
        Fahrenheit= round((float(Celsius)*9/5)+32, 2)
        print(f'{Celsius}°C is equivalent to {Fahrenheit}°F')
    else:
        print(f'Error:Temperature below absolute zero (-273.15°C)') 
    answer=input('Do you want to continue? (yes/no)\n')
    answer=answer.lower()   