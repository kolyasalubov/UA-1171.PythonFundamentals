n = int(input("n: "))
fib = [0, 1]

while fib[-1] + fib[-2] <= n:
    f = fib[-1] + fib[-2]
    fib.append(f)
    print(f, end=" ")