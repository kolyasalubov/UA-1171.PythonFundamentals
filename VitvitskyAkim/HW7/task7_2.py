def area_of_a_rectangle(lenght  = 0,width = 0) :
    """function to calculate the area of a rectangle"""
    return lenght*width
def area_of_a_circle(radius = 0) :
    """function to calculate the area of a circle"""
    PI = 3.14
    return PI * radius ** 2
def area_of_a_triangle(base = 0, height = 0) :
    """function to calculate the area of a triangle"""
    return (base*height)/2

choice = input ("The area of ​​which figure do you want to count?\n\
                Triangle / Circle / Rectangle : ")
match choice.lower():
    case "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(area_of_a_triangle(base,height))
    case "circle":
        radius = float(input("Enter radius: "))
        print(area_of_a_circle(radius))
    case "rectangle":
        lenght = float(input("Enter lenght: "))
        width = float(input("Enter width: "))
        print(area_of_a_rectangle(lenght,width))