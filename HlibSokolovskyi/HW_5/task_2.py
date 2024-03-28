a, b = 0, 1

wanted_number = int(input("Enter wanted number: "))

print("Fibonacci sequence up to the entered number: ")
fib_list = [a, b]
while b < wanted_number:
    a, b = b, a+b
    if b>=wanted_number:
        break
    fib_list.append(b)

print(fib_list)