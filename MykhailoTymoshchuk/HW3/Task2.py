#З даним фрагментом в мене виникли певні трабли, в силу моєї гуманітарії =D 
#тому буду чесним - робив із допомогою АІ (та поясненням детально кроків)
def product_of_digits(number):
    product = 1
    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10
    return product

#Перетворюємо число в стрінгу та повертаємо реверсом
def reverse_number(number):
    return int(str(number)[::-1])

#Сортування числа по зростанню,методом перетворення в рядок
def sorted_digits_asc(number):
    sorted_digits = sorted(str(number)) # перетворюєом рядок в стрінгу і сортуємо
    sorted_number = int("".join(sorted_digits))#Повертаємо відстортований рядок в число
    return sorted_number #Повертаємо нову змінну з відстортованим числом

#Функція яка буде це все викликати в консолі 
def main():
    num = int(input("Write 4digit value: "))
    product = product_of_digits(num)
    reverse_num = reverse_number(num)
    sorted_num = sorted_digits_asc(num)
    
    print("digit:", product)
    print("reverse:", reverse_num)
    print("sorted:", sorted_num)

if __name__ == "__main__":
    main()