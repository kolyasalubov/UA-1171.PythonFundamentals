from functions import *

mark = True

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