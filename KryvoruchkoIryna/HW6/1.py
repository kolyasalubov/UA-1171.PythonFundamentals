list_even_2 = []
list_even_3 = []
list_simple_numbers = []

for i in range(1, 10):
    if i % 2 == 0:
        list_even_2.append(i)
    if i % 2 != 0 and i % 3 == 0:
        list_even_3.append(i)
    if i % 2 != 0 and i % 3 != 0:
        list_simple_numbers.append(i)

print(f'Even numbers: {list_even_2}')
print(f'Odd numbers, which are divisible by 3: {list_even_3}')
print(f'Numbers that are not divisible by 2 and 3: {list_simple_numbers}')