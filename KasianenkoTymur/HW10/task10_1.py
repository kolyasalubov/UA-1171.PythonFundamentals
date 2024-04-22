from random import randint

class Polygon:
    def __init__(self, sides):
        self.sides = sides
    def perimeter(self):
        return sum(self.sides)

class Rectangle(Polygon):
    def __init__(self, hight, width):
        super().__init__([hight, width, hight, width]) 
    def area(self):
        return self.sides[0] * self.sides[1]

while True:
    random_Rectangle = Rectangle(randint(1,20), randint(1,20))
    print(f'Area of the rectangle: {random_Rectangle.area()} cm^2.')

    answer=input('try again? (y/n)\n')
    if answer=='n':
        break