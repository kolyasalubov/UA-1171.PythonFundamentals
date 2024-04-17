######## 1 #######
class Ball(object):
    # your code goes here
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
######## 2 #######
import random
class Ghost(object):
    colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = random.choice(self.colors)
######## 3 #######
def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return (adam, eve)
    
    
class Human():
    def __init__(self, name):
        self.name = name
        
class Man(Human):
    def __init__(self, name):
        super().__init__(name)
        
class Woman(Human):
    def __init__(self, name):
        super().__init__(name)
######## 4 #######
class Person:
    def __init__(self, name, age):
        self.info=f"{name}s age is {age}"
######## 5 #######
from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
        
    def get_mass(self):
        return self.mass
        
    def get_volume(self):
        self.volume = (4/3) * pi * self.radius ** 3
        return self.volume
        
    def get_surface_area(self):
        return 4 * self.radius ** 2 * pi
        
    def get_density(self):
        return self.mass / self.volume
######## 6 ########
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("error")
    cls.__name__ = new_name
###################