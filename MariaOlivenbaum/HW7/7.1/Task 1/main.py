import functions

print(functions.largest_number.__doc__)

first_number = int(input("Please enter first number: "))
second_number = int(input("Please enter second number: "))

largest_number_result = functions.largest_number(first_number, second_number)

print(f"The largest number is {largest_number_result}.\n")


