class Polygon:
    pass

class Rectangle(Polygon):
    length = 0
    width = 0
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def find_area(self):
        return self.length * self.width
    

############# Exaample usage ############# 

rect1 = Rectangle(10, 7)
area_rect1 = rect1.find_area()
print(area_rect1)