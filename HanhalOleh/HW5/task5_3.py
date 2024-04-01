number = int(input("Enter number you want to know a factorial of: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} equals: {factorial}")


