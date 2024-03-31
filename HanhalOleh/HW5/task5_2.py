def fibonacci_sequence(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        next_number = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_number)
    return fibonacci

n = int(input("Enter number: "))
result = fibonacci_sequence(n)
print(f"Fibonacci sequence up to entered number: {result}")