def factorial(x):
    if x == 0 or x == 1:
        return 1
    else: 
        return x * factorial(x-1)

while True:
    num = int(input("Enter non-negative number: \n"))

    if num < 0:
        print("\nInvalid input, try again.\n")
    else: 
        break

print(f"Factorial {num}! = {factorial(num)}")