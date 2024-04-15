import math

class Polygon():

    def __init__(self, num_sides):
        self.num_sides = num_sides
        
    def whatFigure(self):
        if self.num_sides == 3:
            return "Triangle"
        elif self.num_sides == 4:
            return "Square"
        else: return "Polygon"
        
    def sidesValue(self):
        return self.num_sides
    
    def area(self):
        return "No Area"
    
class Rectangle(Polygon):
    
    def __init__(self,height,width):
        Polygon.__init__(self,4)
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width

class Triangle(Polygon):
    
    def __init__(self,base,height):
        Polygon.__init__(self,3)
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    
def main():
        while True: 
            figure_name = str(input("What we count now? Enter 'rectangle', 'triangle'  or write 'quit' for exit: "))
 
            if figure_name == 'rectangle':
                height = float(input("Write height: "))
                width = float(input("Write weight: "))
                result_rectangle = Rectangle(height,width)
                print("Rectangle area: ", result_rectangle.area())
                
            elif figure_name == 'triangle':
                base = float(input("Write base: "))
                height = float(input("Write height: "))
                result_triangle = Triangle(base, height)
                print("Triangle area: ", result_triangle.area())
                
            elif figure_name == 'quit':
                break
            
            else:
                figure_name != 'rectangle' and figure_name != 'triangle'
                print("Invalid vigure name.Please enter 'rectanle' or 'triangle' or 'quit' for exit: ")
                    
if __name__ == '__main__':
    main()
                
                
                
        # height = float(input("Write height: "))
# width = float(input("Write weight: "))
# area_result = Rectangle(height,width)
# print ("Rectangle area: ", area_result.area())
    