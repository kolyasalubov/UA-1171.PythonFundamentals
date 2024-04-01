Fibonacci_input = [int(input(f"input {i+1} number: ")) for i in range(2)]
Fibonacci_numbers = Fibonacci_input[:]
for item in range(int(input("enter number n: "))):   
   Fibonacci_numbers.append(Fibonacci_numbers[item+1]+Fibonacci_numbers[item])
print(Fibonacci_numbers)    