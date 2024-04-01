# 2 fibonacci

mark = True

while mark:
    input_number_fib = int(input('Enter not a negative number: '))
    if input_number_fib < 0:
        print('Invalid input. You should enter a positive number')
    else:
        mark = False


# # 2 fibonacci/1
def fibonacci_up_to_input_number_fib(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

fibonacci_up_to_input_number_fib(input_number_fib)

# # 2 fibonacci/2
index = 2
fibonacci_list = [0, 1]

while index >= 2:
    if input_number_fib == 0:
        fibonacci_list.clear()
        fibonacci_list.append(0)
        break
    elif input_number_fib == 1:
        fibonacci_list.append(1)
        break
    else:
        fibonacci_next = fibonacci_list[index - 1] + fibonacci_list[index - 2]
        if fibonacci_next <= input_number_fib:
            fibonacci_list.append(fibonacci_next)
            index += 1
        else:
            break

print(f'Fibonacci numbers: {fibonacci_list}')