from math import pi
def areaRectangle(a:float, b:float):
    """calculate the area of a rectangle
    
    a:type(float) - Breadth
    b:type(float) - Length
    
    return:type(float) area of a rectangle"""
    
   
    return f'area of a rectangle = {a * b}'

def areaTriangle(Base:float, Height:float):
    """calculate the area of a Triangle
    
    Base - type(float)
    Height - type(float)
    
    return:type(float) area of a Triangle"""
    
    return f'area of a Circle = {1/2 * Base * Height}'
def areaCircle(radius:float):
    """calculate the area of a Circle
    
    radius:type(float) - circle radius
    
    return:type(float) area of a Circle"""
    
    return f'area of a Circle = {pi * (radius**2)}'

def get_user_choice(choice):

        match choice:
            case '1':
                return(areaRectangle(float(input("input Breadth ")), float(input("input Length "))))
            case '2':
                return(areaTriangle(float(input("input Base ")), float(input("input Height "))))
            case '3':
                return(areaCircle(float(input("input radius "))))
            case _:
                return "error"
    
