import operation

choice = int(input("Enter 1,2,3: "))
if choice == 1:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = operation.rectangle_area(length, width)
    print(area)
elif choice == 2:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = operation.triangle_area(base, height)
    print(area)
elif choice == 3:
    radius = float(input("Enter the radius: "))
    area = operation.circle_area(radius)
    print(area)