def triangle_area(a, h):
    area = 0.5 * a * h
    return f"area of the triangle is: {area}"

def rectangle_area(a, b):
    area  = a * b
    return f"area of the rectangle is: {area}"

def circle_area(r):
    area = 3.14 * r**2
    return f"area of the circle is: {area}"

while True:

    choice = input("What shape do you want to know the area of?\n1 - Triangle\n2 - Rectangle\n3 - Circle\n4 - Leave\n")

    if choice == "1":
        a = int(input("what is the side of the triangle on which the altitude is lowered? "))
        h = int(input("what is the altitude?"))
        print(triangle_area(a, h))
        
    elif choice == "2":
        a = int(input("what is the longer side of the rectangle?"))
        b = int(input("what is the shorter side of the rectangle?"))
        print(rectangle_area(a, b))

    elif choice == "3":
        r = int(input("what is the radius of the circle?"))
        print(circle_area(r))
    
    elif choice == "4":
        print("bye-bye!")
        break

    else:
        print("Wrong number\n")

