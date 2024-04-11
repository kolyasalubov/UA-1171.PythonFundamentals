import area_claculation as area

def choose_figure():
    command = int(input("""Please select the area of what you want to calculate now?
    1 - rectungle
    2 - triangle
    3 - circle
    """))

    match command:
        case 1:
            rect_length = float(input("Please enter the length of rectangle: "))
            rect_breadth = float(input("Please enter the breadth of rectangle: "))
            rect_area = area.comp_area_of_rectangle(rect_length, rect_breadth)
            print(f"The area of rectangle with sides {rect_length} "
                  f"and {rect_breadth} is {rect_area}.")
        case 2:
            triangle_base = float(input("Please enter the base of triangle: "))
            triangle_height = float(input("Please enter the height of triangle: "))
            triangle_area = area.comp_area_of_triangle(triangle_base, triangle_height)
            print(f"The area of triangle with base {triangle_base} "
                  f"and height {triangle_height} is {triangle_area}.")
        case 3:
            circle_radius = float(input("Please enter the radius of circle: "))
            circle_area = area.comp_area_of_circle(circle_radius)
            print(f"The area of circle with radius {circle_radius} is {circle_area}.")
        case _:
            print("Wrong figure.")

