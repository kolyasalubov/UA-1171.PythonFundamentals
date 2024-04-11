# Таска1
# Визначаємо список парних чисел, які діляться на 2
even_divisible_by_2 = []
for num in range(1, 11):
    if num % 2 == 0:
        even_divisible_by_2.append(num)

# Визначаємо список непарних чисел, які діляться на 3
odd_divisible_by_3 = []
for num in range(1, 11):
    if num % 2 != 0 and num % 3 == 0:
        odd_divisible_by_3.append(num)

# Визначаємо список чисел, які не діляться ані на 2, ані на 3
not_divisible_by_2_and_3 = []
for num in range(1, 11):
    if num % 2 != 0 and num % 3 != 0:
        not_divisible_by_2_and_3.append(num)



# Таска 2
def check_login():
    while True:
        login = input("Enter your login: ")  # Просимо користувача ввести логін
        if login == "First":  # Якщо введений логін - "First"
            print("Welcome, user!")  # Привітати користувача
            break  # Вийти з циклу, якщо логін вірний
        else:
            print("Error: Invalid login. Please try again.")  # Якщо введений невірний логін, вивести повідомлення про помилку і продовжити цикл
