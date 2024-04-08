
# #Rectangle area calculate
# def rectangleAreaCalculate(length, width):
#     return length * width

# length = float(input("Whrite length of rectangle: "))
# width = float(input("Whrite width of rectangle: "))

# area = rectangleAreaCalculate(length, width)
# print("Rectangle Area: ", area)



# #Triangle area calculate
# def triangleAreaCalculate(base, heigth):
#     return 0.5 * base * heigth

# base = float(input("Whrite base of triangle: "))
# heigth = float(input("Whrite heigth of triangle: "))

# area = triangleAreaCalculate(base, heigth)
# print("Triangle Area: ", area)

#Circle area calculate

import math

def circleAreaCalculate(radius):
    return math.pi * radius ** 2

radius = int(input("Whire radius for calc: "))

area = circleAreaCalculate(radius)
print("Circle area: ", area)
    