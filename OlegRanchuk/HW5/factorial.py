num = int(input("Enter number: "))

if num < 0:
    print("Factorial is not defined for negative numbers!")
else:
    factor = 1

for i in range(2, num + 1):
    factor *= i
print(f"{num} = {factor}")
