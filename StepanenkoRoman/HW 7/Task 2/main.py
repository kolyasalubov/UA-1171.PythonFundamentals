"""Task2. Write a program that calculates the area of a rectangle, 
triangle and circle (write three functions to calculate the area. 
And call them in the main program depending on the user's choice)."""

from math import pi

def rectangleArea(rect_length, rect_width):
    return rect_length * rect_width

def triangleArea(triangle_base, triangle_height):
    return 0.5 * triangle_base * triangle_height

def circleArea(circle_radius):
    return round(pi * circle_radius**2, 2)


user_number = int(input("Choose the area which figure calculates: 1 Rectangle, 2 Triangle, 3 Circle "))

match user_number:
   
    case 1:
        rect_lenght = float(input("Choose rect_lenght "))
        rect_width = float(input("Choose rect_wiedth "))
        area_rec = rectangleArea(rect_lenght, rect_width)
        print(f"rectangleArea is: {area_rec}")

    case 2:  
        triangle_base = float(input("Choose triangle_base "))
        triangle_height = float(input("Choose triangle_height "))
        area_tri = triangleArea(triangle_base, triangle_height)
        print(f"Area of traingle is: {area_tri}")

    case 3:
        circle_radius = float(input("Please choose circle_radius "))
        area_circ = circleArea(circle_radius)
        print(f"The Circus area is: {area_circ}")
    case _:
        print("ERROR choice correct number")

