# # Таска 1
class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def area(self):
        pass  # Цей метод буде перевизначено у підкласах


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(num_sides=4)  # Прямокутники мають 4 сторони
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Приклад використання:
rectangle = Rectangle(length=5, width=4)
print("Площа прямокутника:", rectangle.area())  # Вивід: 20



# # Таска 2
class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Wellcome stranger, {self.name}!"

    @classmethod
    def species_info(cls):
        return "This is a kind of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "But who knows nowadays whether he is a man or a woman, or whether they are even <they>?"


# Приклад використання:
names = ["Sirco","Benicio"]

for name in names:
    human = Human(name)


print(human.welcome_message())  # Вивід: Ласкаво просимо, {name}!

print(Human.species_info())  # Вивід: Це вид Homosapiens.

print(Human.arbitrary_message())  # Вивід: Це статичний метод. 

#   Додатково даю метод введення з терміналу так як не зрозумів задачу
# Введення імен з терміналу
names = input("Введіть імена людей через кому: ").split(", ")

# Створення екземплярів класу Human для кожного введеного імені
for name in names:
    human = Human(name)
    print(human.welcome_message())  # Вивід: Ласкаво просимо, {ім'я}!



# Таска 3
class Employee:
    # Лічильник загальної кількості співробітників
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # Збільшення лічильника при створенні нового співробітника
        Employee.total_employees += 1

    @staticmethod
    def display_total_employees():
        # Виведення загальної кількості співробітників
        print(f"Загальна кількість співробітників: {Employee.total_employees}")

    def display_info(self):
        # Виведення інформації про кожного співробітника
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")


# Приклад використання класу Employee
employee1 = Employee("Іван", 5000)
employee2 = Employee("Петро", 6000)

# Виведення загальної кількості співробітників
Employee.display_total_employees()

# Виведення інформації про кожного співробітника
employee1.display_info()
employee2.display_info()

# Відображення інформації про базові класи, простір імен класу, ім'я класу та модуль, де визначений клас, і документації
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)