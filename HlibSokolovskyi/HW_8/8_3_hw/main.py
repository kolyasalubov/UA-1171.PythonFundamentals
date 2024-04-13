import area
    
while True:
    choice = input("What figure area you want to know? \nRectangle - 1 \nTriangle - 2\nCircle - 3 \nExit program - e\n")
    match choice:
        case "1":
            a=float(input("Enter sides of the rectangle: "))
            b=float(input())
            if a > 0 and b > 0:
                print(f"The rectangle area is {area.rectangle(a, b)}")
                break
            else:
                print("\nInvalid values, try again.\n")
        case "2":
            h = float(input("Enter height of the triangle: "))
            a = float(input("Enter base of the triangle: "))
            if a > 0 and h > 0:
                print(f"The triangle area is {area.triangle(h, a)}")
                break
            else:
                print("\nInvalid values, try again.\n")
        case "3":
            r = float(input("Enter radius of the circle: "))
            if r > 0:
                print(f"The circle area is {area.circle(r)}")
                break
            else:
                print("\nInvalid value, try again.\n")
        case "e":
            break
        case _:
            print("\nInvalid input, try again.\n")