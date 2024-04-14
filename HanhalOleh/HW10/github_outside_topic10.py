########## 1 ##########

class Ball(object):
    ball_type = None
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

########## 2 ##########

import random
class Ghost(object):
    color = None
    colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = random.choice(self.colors)

########## 3 ##########

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        self.name = name

class Woman(Human):
    def __init__(self, name):
        self.name = name

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return (adam, eve)

########## 4 ##########

class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

########## 5 ##########

from math import pi

class Sphere(object):
    def __init__(self, r, m):
        self.radius = r
        self.mass = m
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return 4/3 * pi * self.radius**3
    
    def get_surface_area(self):
        return 4 * pi * self.radius**2
    
    def get_density(self):
        return self.mass / (4/3 * pi * self.radius**3)

########## 6 ##########

def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid class name. Class names should start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name