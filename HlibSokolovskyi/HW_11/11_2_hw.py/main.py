import functions

try:
    number = str(input("Enter an integer from 1 to 7: "))
    functions.number_analyze(number)
except ValueError as e:
    print("Error:", e)