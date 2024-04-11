import area_formula

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
        print(area_formula.rectangle_area(length, width))
        
    elif answer == "2":
        base = float(input("base: "))
        height = float(input("height: "))
        print(area_formula.triangle_area(base, height))

    elif answer == "3":
        radius = float(input("radius: "))
        print(area_formula.circle_area(radius))
    
    elif answer == "4":
        break

    else:
        print("Wrong number!\n")