class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width]) 

    def area(self):
        return self.sides[0] * self.sides[1]

myRectangle = Rectangle(5, 3)
print("Area of the rectangle:", myRectangle.area())
