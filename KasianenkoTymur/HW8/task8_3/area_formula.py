from math import pi 
def rectangle_area(length , width):
    area = length * width
    return f"area of the rectangle is: {area}"

def triangle_area(base, height):
    area = 0.5 * base * height
    return f"area of the triangle is: {area}"

def circle_area(radius):
    area = round((pi * pow(radius, 2)), 2)
    return f"area of the circle is: {area}"