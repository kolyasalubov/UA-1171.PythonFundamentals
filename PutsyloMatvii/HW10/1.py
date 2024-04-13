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

    def square(self):
        return self.sides[0] ** 2


rect = Rectangle(5, 3)
print("Perimeter", rect.perimeter())
print("Area", rect.area())
print("Square", rect.square())
