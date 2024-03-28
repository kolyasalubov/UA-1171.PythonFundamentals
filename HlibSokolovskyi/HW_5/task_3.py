your_number = int(input("Enter non-negative number: "))
if your_number == 0 or your_number == 1:
    print(f"{your_number}! = 1")
elif your_number < 0:
    print("Error: entered number is less than 0")
else: 
    wanted_factorial = 1
    for i in range(1, your_number+1):
        wanted_factorial*=i
    
    print(f"{your_number}! = {wanted_factorial}")