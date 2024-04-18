# # 1 Ball_syper_ball
# # Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# # If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

# class Ball:
#     def __init__(self, ball_type='regular'):
#         self.ball_type = ball_type

# # Example usage
# regular_ball = Ball()
# print(regular_ball.ball_type)  # Output: regular

# football = Ball('super')
# print(football.ball_type) 



# # 2 Color Ghost
# # Create a class Ghost
# # Ghost objects are instantiated without any arguments.
# # Ghost objects are given a random color attribute of "white" 
# # or "yellow" or "purple" or "red" when instantiated
# import random

# class Ghost:
#     def __init__(self):
#         self.color = random.choice(['white', 'yellow', 'purple', 'red'])

# # Example usage
# ghost1 = Ghost()
# print(ghost1.color)  # Output: one of 'white', 'yellow', 'purple', 'red'

# ghost2 = Ghost()
# print(ghost2.color) 


# # 3 According to the creation myths of the Abrahamic religions, 
# # Adam and Eve were the first Humans to wander the Earth.
# # You have to do God's job. The creation method must return an array of 
# # length 2 containing objects (representing Adam and Eve). The first 
# # object in the array should be an instance of the class Man. The second 
# # should be an instance of the class Woman. Both objects have to be 
# # subclasses of Human. Your job is to implement the Human, Man and Woman 
# # classes.

# class Human:
#     def __init__(self, name):
#         self.name = name

# class Man(Human):
#     def __init__(self, name):
#         super().__init__(name)

# class Woman(Human):
#     def __init__(self, name):
#         super().__init__(name)

# def create():
#     adam = Man("Adam")
#     eve = Woman("Eve")
#     return [adam, eve]

# person = Man
# person = Woman

# paradise = God.create()
# for person in paradise:
#     print(f"{person.name} is a {type(person).__name__}")



# 4 Your task is to complete this Class, the Person class has been created.
#  You must fill in the Constructor method to accept a name as string and 
#  an age as number, complete the get Info property and getInfo method/Info
#  getter which should return johns age is 34

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @property
#     def info(self):
#         return f"{self.name}s age is {self.age}"

#     @info.setter
#     def info(self, value):
#         name, _, age_str = value.partition("s age is ")
#         if age_str.isdigit():
#             self.name = name
#             self.age = int(age_str)

# # Example usage:
# john = Person("John", 34)
# print(john.info)  # Output: John's age is 34

# # Changing information using the setter
# john.info = "Alice's age is 28"
# print(john.info)  # Output: Alice's age is 28



# # 4 Now that we have a Block let's move on to something slightly more complex: a Sphere.

# # Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
# # Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
# # Example
# ball = Sphere(2,50)
# ball.get_radius() ->       2
# ball.get_mass() ->         50
# ball.get_volume() ->       33.51032
# ball.get_surface_area() -> 50.26548
# ball.get_density() ->      1.49208
# # Any feedback would be much appreciated


# class Sphere(object):
#     pass

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
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

# Example usage
ball = Sphere(2, 50)
print(ball.get_radius())        # Output: 2
print(ball.get_mass())          # Output: 50
print(ball.get_volume())        # Output: 33.51032
print(ball.get_surface_area())  # Output: 50.26548
print(ball.get_density())       # Output: 1.49208
