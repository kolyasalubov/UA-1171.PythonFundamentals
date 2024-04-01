even_numbers=[]
odd_numbers=[]
not_divisible_numbers=[]

for i in range (1,10):
    if i%2==0:
        even_numbers.append(i)
    elif i%2==1 and i%3==0:
        odd_numbers.append(i)
    else:
        not_divisible_numbers.append(i)

print(f'even numbers: {even_numbers}')
print(f'odd numbers and divisible by 3: {odd_numbers}')
print(f'not divisible by 2 and 3: {not_divisible_numbers}')