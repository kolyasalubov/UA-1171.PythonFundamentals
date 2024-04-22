# Regular Ball Super Ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Color Ghost
import random

class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)


# Basic subclasses - Adam and Eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

# Classy Classes
class Person:
    def __init__(self, name, age):
        self.info=f"{name}s age is {age}"


# Building Spheres
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
        volume = (4/3) * math.pi * self.radius ** 3
        return volume

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return surface_area

    def get_density(self):
        density = self.mass / self.get_volume()
        return density


#Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    old_name = cls.__name__
    cls = globals().get(old_name)
    globals()[new_name] = cls
    del globals()[old_name]