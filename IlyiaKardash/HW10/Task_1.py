class Polygon():
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width


class Rectangle(Polygon):
    def find_area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)
result = rectangle.find_area()

print(result)
