"""1)Create empty list
   2)Create form with the desired user value of input numbers
   3)Loop with index ranging on input values of numbers
   4)2nd Input - that accepts numbers
   5)appending this numbers to early created list1
   6)print all accepts number and method max for finding largest number
   """
list1 = []

num = int(input("Enter your number value: "))

for i in range(num):
    number = int(input("Enter number: "))
    list1.append(number)
    
print("Number you entered: ", list1)
print("Largest number is: ", max(list1))