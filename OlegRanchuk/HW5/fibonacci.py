fib_num = int(input("Enter your Fibonacci numbers: "))


a, b = 0, 1

for i in range (fib_num):
    print (a, end=" ")
    a , b = b, a + b 