list1 = []

num = int(input("Enter your number value: "))

for i in range(num):
    number = int(input("Enter number: "))
    list1.append(number)
    
print("Number you entered: ", list1)
print("Largest number is: ", max(list1))