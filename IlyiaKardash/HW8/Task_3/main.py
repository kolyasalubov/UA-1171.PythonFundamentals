import area

print("Calculate the area of following shapes: \n"
      "1. Rectangle \n"
      "2. Triangle \n"
      "3. Circle \n"
      "4. Exit \n")


while True:
    user_input = str(input('Area of which shape do you want to calculate?'))
    if user_input == "Exit":
        print("Bye!")
        break
    elif user_input == "1":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        area = area.areaRectangle(width, height)
        print(f'Area of a rectangle is {area}')

    elif user_input == "2":
        base = int(input("Enter base: "))
        height = int(input("Enter height: "))
        area = area.areaTriangle(base, height)
        print(f'Area of a triangle is {area}')

    elif user_input == "3":
        radius = int(input("Enter radius: "))
        area = area.areaCircle(radius)
        print(f'Area of a circle is {area}')
    else:
        print("Invalid number")
