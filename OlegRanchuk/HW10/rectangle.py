class Polygon:
    def __init__(self, sides):
        self.sides = sides 

class Rectangle(Polygon):
    def __init__(self, lenght, width):
        self.lenght = lenght 
        self.width = width 

    def get_area(self):
        return self.lenght * self.width 
    
rec = Rectangle(7, 4)
area = rec.get_area()
print(f"Area of rectangle {area}")
        