class Polygon():

    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [abs(float(input(f"Enter side {str(i+1)}: "))) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {str(i+1)}: {self.sides[i]}")
    
    # I added the method for calculating perimeter of any figure
    def perimeter(self):
        per = 0
        for side in self.sides:
            per += side
        print(f"Perimeter of the figure: {per}")

        
class Rectangle(Polygon):
    
    def __init__(self):
        Polygon.__init__(self, 4)
        print("Rectangle created.\n")

    def inputSides(self):
        self.sides = [abs(float(input(f"Enter side {str(i+1)}: "))) for i in range(2)]
        self.sides.append(self.sides[0])
        self.sides.append(self.sides[1])

    
    def rect_area(self):
        a, b = self.sides[:2]
        self.area = a*b
        print(f"The area of the rectangle: {self.area}")
