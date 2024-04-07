import math


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return math.pi * (radius ** 2)


choice = int(input("Enter 1,2,3: "))
if choice == 1:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = rectangle_area(length, width)
    print(area)
elif choice == 2:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = triangle_area(base, height)
    print(area)
elif choice == 3:
    radius = float(input("Enter the radius: "))
    area = circle_area(radius)
    print(area)