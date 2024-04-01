# 3 factorial
input_number_fact = int(input('Enter number for calculating factorial: '))

result = 1

if input_number_fact > 0:
    for i in range(1, input_number_fact + 1):
        result *= i
else:
    print(f'Invalid input. You should enter a positive number')

print(f'{input_number_fact}! = {result}')