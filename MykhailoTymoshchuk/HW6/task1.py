numbers = list(range(1,11))

#створюємо пусті контейнери куди будемо append'ити наші числа
even_numbers = []
odd_numbers = []
not_divisible_numbers = []
#функція , яка пробігається по заданому ренджу та робить перевірку "Even" or "Odd" or "Not divisible"
for num in numbers:
    if num %2 == 0:
        even_numbers.append(num)
    elif num %3 == 1:
        odd_numbers.append(num)
    else:
        not_divisible_numbers.append(num)
#Виводимо і щоб красиво було ))
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Not divisible by 2 or 3:", not_divisible_numbers)