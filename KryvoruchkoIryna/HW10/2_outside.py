# # # 1 

class Ball:

    def __init__(self, name="regular"):
        self.name = name
    
ball1 = Ball()
ball2 = Ball("super")

print(ball1.name)
print(ball2.name)

# # # 2
import random

class Ghost:

    colors = ['white', 'yellow', 'purple', 'red']

    def __init__(self):
        self.color = random.choice(self.colors)

ghost_1 = Ghost()
ghost_2 = Ghost()
ghost_3 = Ghost()
ghost_4 = Ghost()
print(ghost_1.color)
print(ghost_2.color)
print(ghost_3.color)
print(ghost_4.color)

# # # 3

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def creation_method():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

create = creation_method()
for obj in create:
    print(obj.name)

# # # 4
    
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name} is {self.age}"

# Example usage
john = Person("John", 34)
print(john.info)

# # # 5 

import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

ball = Sphere(2, 50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())

# # # 6

import re

class ReNameAbleClass:
    def __init__(self):
        pass

    @classmethod
    def change_class_name(cls, new_name):
        if not new_name[0].isupper() or not re.match("^[A-Za-z0-9]*$", new_name):
            raise ValueError("Invalid class name. Must start with uppercase letter and contain only alphanumeric characters.")
        cls.__name__ = new_name

    def __str__(self):
        return f"Class name is: {self.__class__.__name__}"

obj = ReNameAbleClass()
print(obj)

ReNameAbleClass.change_class_name("NewName")
print(obj)

try:
    ReNameAbleClass.change_class_name("newName")
except ValueError as e:
    print(e)