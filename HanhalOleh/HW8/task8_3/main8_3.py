import area_formulas

while True:

    choice = input("What shape do you want to know the area of?\n1 - Triangle\n2 - Rectangle\n3 - Circle\n4 - Leave\n")

    if choice == "1":
        a = int(input("what is the side of the triangle on which the altitude is lowered? "))
        h = int(input("what is the altitude? "))
        print(area_formulas.triangle_area(a, h))
        
    elif choice == "2":
        a = int(input("what is the longer side of the rectangle? "))
        b = int(input("what is the shorter side of the rectangle? "))
        print(area_formulas.rectangle_area(a, b))

    elif choice == "3":
        r = int(input("what is the radius of the circle? "))
        print(area_formulas.circle_area(r))
    
    elif choice == "4":
        print("bye-bye!")
        break

    else:
        print("Wrong number\n")
