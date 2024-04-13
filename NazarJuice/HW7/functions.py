from math import pi
def areaRectangle(a:float, b:float):
    """calculate the area of a rectangle
    
    a - Breadth
    b - Length
    
    return area of a rectangle"""
    
   
    return f'area of a rectangle = {a * b}'

def areaTriangle(Base:float, Height:float):
    """calculate the area of a Triangle
    
    return area of a Triangle"""
    
    return f'area of a Circle = {1/2 * Base * Height}'
def areaCircle(radius:float):
    """calculate the area of a Circle
    
    radius - circle radius
    
    return area of a Circle"""
    
    return f'area of a Circle = {pi * (radius**2)}'