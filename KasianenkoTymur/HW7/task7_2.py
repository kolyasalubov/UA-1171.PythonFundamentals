from math import pi 
def rectangle_area(length , width):
    area = length * width
    return f"area of the rectangle is: {area}"

def triangle_area(base, height):
    area = 0.5 * base * height
    return f"area of the triangle is: {area}"

def circle_area(radius):
    area = round((pi * radius**2), 2)
    return f"area of the circle is: {area}"

while True:

    answer = input("""What area do you want to calculate?
1 - Rectangle
2 - Triangle
3 - Circle
4 - exit
""")

    if answer == "1":
        length  = float(input("length: "))
        width = float(input("width: "))
        print(rectangle_area(length, width))
        
    elif answer == "2":
        base = float(input("base: "))
        height = float(input("height: "))
        print(triangle_area(base, height))

    elif answer == "3":
        radius = float(input("radius: "))
        print(circle_area(radius))
    
    elif answer == "4":
        break

    else:
        print("Wrong number!\n")