from class_Rectangle import Rectangle

rect_length = float(input("Enter the length of rectangle: "))
rect_width = float(input("Enter the width of rectangle: "))

first_rectangle = Rectangle(rect_length, rect_width)

print(round(first_rectangle.area(), 2))
