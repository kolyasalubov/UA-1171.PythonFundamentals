from math import sqrt
from math import pi

def rectangle(side1, side2):
    return round(side1*side2, 2)


def triangle(side1, side2, side3):
    p = (side1 + side2 + side3)/2
    return round(sqrt(p*(p-side1)*(p-side2)*(p-side3)), 2)


def circle(radius):
    return round(pi*(radius**2), 2)
    
while True:
    choice = input("What figure area you want to know? \nRectangle - 1 \nTriangle - 2\nCircle - 3 \nExit program - e\n")
    match choice:
        case "1":
            a=float(input("Enter sides of the rectangle: "))
            b=float(input())
            if a > 0 and b > 0:
                print(f"The rectangle area is {rectangle(a,b)}")
                break
            else:
                print("\nInvalid values, try again.\n")
        case "2":
            a = float(input("Enter sides of the triangle: "))
            b = float(input())
            c = float(input())  
            if a > 0 and b > 0 and c > 0:
                if a + b > c and a + c > b and b + c > a:
                    print(f"The triangle area is {triangle(a,b,c)}")
                    break
                else:
                    print("\nInvalid values, try again.\n")
            else:
                print("\nInvalid values, try again.\n")
        case "3":
            r = float(input("Enter radius of the circle: "))
            if r > 0:
                print(f"The circle area is {circle(r)}")
                break
            else:
                print("\nInvalid value, try again.\n")
        case "e":
            break
        case _:
            print("\nInvalid input, try again.\n")