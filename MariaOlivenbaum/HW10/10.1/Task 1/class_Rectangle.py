from class_Polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, length, width):
        self.num_of_sides = 4
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
