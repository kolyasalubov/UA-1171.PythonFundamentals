''' Task 3.
Write a program that calculates the area of a rectangle S=a*b, 
the area of a triangle S=0.5*h*a, the area of a circle S=pi***2. 
This module must be used in another module in which we ask the user
the area of which figure he wants to calculate.
(To perform the task, you need to import the math module, and from
it the pow() function and the value of the variable pi, and module,
which contains three functions for finding areas, into the main program.
The basic logic of the program is executed in the main.'''

from area_calc_func import area_triangle
from area_calc_func import area_rectangle
from area_calc_func import area_circle



user_number = int(input("""Choose the area which figure calculates: 
        Rectangle (1) 
         Triangle (2) 
           Circle (3):  """))

match user_number:
   
    case 1:
        rect_lenght = float(input("Please choose your rectangle lenght:  "))
        rect_width = float(input("Please choose your rectangle wiedth:  "))
        area_rec = area_rectangle(rect_lenght, rect_width)
        print(f"The area of your rectangle is: {area_rec}")

    case 2:  
        triangle_base = float(input("Please choose your triangle base:  "))
        triangle_height = float(input("Please choose your triangle height:  "))
        area_tri = area_triangle(triangle_base, triangle_height)
        print(f"The area of your traingle is: {area_tri}")

    case 3:
        circle_radius = float(input("Please choose you circle radius: "))
        area_circ = area_circle(circle_radius)
        print(f"The your circus area is: {area_circ}")
    case _:
        print("ERROR choice correct number")


