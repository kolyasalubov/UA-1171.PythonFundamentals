# YuriiYevpakHW7


#     #   Task1 (функція що повертає максимальне число з двох чисел)

def bigs_numbs(num1, num2):
    """
    Повертає більше з двох чисел.

    Параметри:
    num1 (int or float): Перше число.
    num2 (int or float): Друге число.

    Повертає:
    int or float: Більше з двох чисел.
    """
    return max(num1, num2)


print(bigs_numbs(32, 3))



#     #   Task 2(Прорама що дає користовачу можливіть 
#     #   вводячи дані порахувати площу круга, прямокутника та трикутника)
import math

def area_triangle(base, height):
    product_for_triangel = (base * height)
    area_triangle = product_for_triangel / 2
    return area_triangle
    
def area_circle(radius):
    square_of_radius = (radius * radius)
    pi_number = 3.14
    area_circle = (pi_number * square_of_radius)
    return area_circle
    
def area_rectangle(length, width):
    area_rectangle = length * width
    return area_rectangle


def main():
    print("Виберіть фігуру для обчислення площі:") 
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Ваш вибір (1/2/3): ")

    if choice == '1':
        length = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))
        area = area_rectangle(length, width)
        print("Площа прямокутника:", area)
    elif choice == '2':
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        area = area_triangle(base, height)
        print("Площа трикутника:", area)
    elif choice == '3':
        radius = float(input("Введіть радіус кола: "))
        area = area_circle(radius)
        print("Площа кола:", area)
    else:
        print("Неправильний вибір. Будь ласка, виберіть знову.")

if __name__ == "__main__":
    main()



#        Task 3(Функція для обчислення символів в рядку)
def count_characters():
    input_string = input("Введіть рядок: ")
    
    char_count = {}
    
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

result = count_characters()
print(result)
