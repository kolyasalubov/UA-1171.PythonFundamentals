
2.1

your_number = int(input("Enter 4-digit number: "))
str_number = str(your_number)
if len(str_number) != 4:
    print("Error: You entered not 4-digit number.")
else:
    product = 1
    for i in range(4):
        x = int(str_number[i])
        product*=x

print(f"Product of the digits of this number: {product}")


2.2

reversed_number = int(str(your_number)[::-1])

print(f"Reverse number: {reversed_number}")

