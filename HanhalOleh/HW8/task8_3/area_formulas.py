from math import pi

def triangle_area(a, h):
    area = 0.5 * a * h
    return f"area of the triangle is: {area}"

def rectangle_area(a, b):
    area  = a * b
    return f"area of the rectangle is: {area}"

def circle_area(r):
    area = pi * r**2
    return f"area of the circle is: {area}"