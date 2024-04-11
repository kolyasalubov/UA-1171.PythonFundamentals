import random

amount=random.randint(5,10)
list_integer_numbers=[]

for i in range(amount):
    list_integer_numbers.append(random.randint(1,1000))

print(f'integet numbers:{list_integer_numbers}')

list_floating_numbers=[]

for number in list_integer_numbers:
    list_floating_numbers.append(float(number))

print(f'floating numbers:{list_floating_numbers}')