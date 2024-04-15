import math 
""" 
Program that calculate area of rectangles(or other figure`s) using:
1)class Polygon (momy)
2)class Rectangle(daugther)
"""

#Створюємо клас Polygon ініціалізуємо , та задаємо параметри які визначать які фігура буде обраховуватись
class Polygon:
    
    def __init__(self,numsides):
        self.num_sides = numsides #
        
    def whatFigure(self):
        if self.num_sides == 3:
            return "Triangle"
        elif self.num_sides == 4:
            return "Rectangle"
        else: return "Polygon"
# етап який повертає кількість сторін        
    def howManySides(self):
        return self.num_sides
#якщо немає даних - поверне , що немає і обрахунку площі
    def area(self):
        return 'No Area'
# class Rectangle - який наслідує головний , та приймає його параметри.   
class Rectangle(Polygon):
    def __init__(self,length,width):
         Polygon.__init__(self,4)
         self.length = length
         self.width = width
# формула для обрахунку прощі прямокутника         
    def area(self):
        return self.length * self.width

# форма , яка запитує які значення треба обрахувати
length = float(input("Whrite length of rectangle: "))
width = float(input("Whrite width of rectangle: "))
result = Rectangle(length,width)
print("Rectangle area: ", result.area())