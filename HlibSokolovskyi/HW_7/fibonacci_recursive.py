def fib(x, fib_seq=[0,1]):
    if fib_seq[-1] > x:
        return fib_seq[:-1]       
    else: 
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib(x, fib_seq)

while True:
    num = int(input("Enter non-negative number: \n"))

    if num < 0:
        print("\nInvalid input, try again.\n")
    else: 
        break


print(f"Fibonacci sequence to the {num}:\n {fib(num)}")