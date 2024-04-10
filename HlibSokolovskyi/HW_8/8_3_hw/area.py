from math import pi
from math import pow

def rectangle(side1, side2):
    return round(side1*side2, 2)


def triangle(height, base):
    return round(0.5*base*height, 2)


def circle(radius):
    return round(pi*pow(radius, 2), 2)