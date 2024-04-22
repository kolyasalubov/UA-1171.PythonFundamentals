import functions

try:
    age = int(input("Enter your age: "))
    functions.process_age(age)
except ValueError as e:
    print("Error: ", e)
