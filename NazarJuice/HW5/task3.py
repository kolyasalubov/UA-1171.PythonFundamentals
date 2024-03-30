flag = True
while flag:
    number = int(input("Enter number: "))

    factorial = 1

    if number == 0:
        print("factorial = 1")
    elif number <= 0 :
        print("fail: enter natural number")
    else:
        for i in range(1,number+1):
            factorial *= i
        print("factorial = ", factorial)    
    if input('Enter "yes" if you wont to end ') == "yes":
        flag = False    
    
    