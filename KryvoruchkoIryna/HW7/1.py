# # 1

def find_more(a, b):
    if a > b:
        return a
    else:
        return b

mark = True

while mark:
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))

    if first_number != second_number:
        print(f'The largest number of two numbers: {find_more(first_number, second_number)}')
    else:
        print('You should enter only numbers!')

    user_ans = input('Do you want to start again? y / n \n')
    if user_ans == 'n':
        mark = False

# # 2
# area of rectangle = length × width
# Area of a Triangle = A = ½ (base × height)
# Area of circle formula = π × r2

mark = True

PI = 3.14
def area_of_restangle(length, width):
    return length * width

def area_of_triangle(base, height):
    return (0.5 * base * height)

def area_of_circle(r):
    return PI * r**2

while mark:
    operations = input("""What operation do you want to do?
                       1. Area of rectangle
                       2. Area of a Triangle
                       3. Area of Circle formula
                       Please enter number of operations: """)

    match operations:
        case '1':
            length = float(input('Enter length of rectangle: '))
            width = float(input('Enter width of rectangle: '))
            print(f'Area of rectangle: {area_of_restangle(length, width)}')
        case '2':
            base = float(input('Enter base of triangle: '))
            height = float(input('Enter height of triangle: '))
            print(f'Area of a Triangle: {area_of_triangle(base, height)}')
        case '3':
            r = float(input('Enter radius of circle: '))
            print(f'Area of Circle formula: {area_of_circle(r)}')
        case _:
            print('You should enter only numbers! 1-3')

    user_ans = input('Do you want to start again? y / n \n')
    if user_ans == 'n':
        mark = False

# # 3

start_str = 'hello world'
list_str = list(start_str)
result_dict = {}

for index in range(len(start_str)):
    if start_str[index] in result_dict:
        result_dict[start_str[index]] += 1
    else:
        result_dict[start_str[index]] = 1

print(result_dict)