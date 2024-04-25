"""1.1"""


# class Ball():
#     def __init__(self, ball_type="regular") -> None:
#         self.ball_type = ball_type

#     def __str__(self) -> str:
#         return f'A {self.ball_type} ball'


# ball1 = Ball()
# ball2 = Ball("super")
# print(ball1.ball_type)
# print(ball2.ball_type)

"""1.2"""


# import random
# class Ghost():
#     colors = ['white', 'yellow', 'purple', 'red']

#     def __init__(self) -> None:
#         self.color = self.random_color()

#     def random_color(self):
#         return random.choice(Ghost.colors)


# ghost = Ghost()
# print(ghost.color)  # => "white" or "yellow" or "purple" or "red"


"""1.3"""


# class Human():
#     def __init__(self, name) -> None:
#         self.name = name

#     def __str__(self) -> str:
#         return self.name


# class Man(Human):
#     def __init__(self, name) -> None:
#         super().__init__(name)


# class Woman(Human):
#     def __init__(self, name) -> None:
#         super().__init__(name)


# def God():
#     adam = Man("Adam")
#     eve = Woman("Eve")
#     return [adam, eve]


# if __name__ == "__main__":
#     adam, eve = God()
#     print(f'First human is {adam}, second is {eve}')


"""1.4"""


# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info = f'{name}s age is {age}'


# person = Person("John", 34)
# print(person.info)


"""1.5"""


# import math
# class Sphere():
#     def __init__(self, radius, mass) -> None:
#         self.radius = radius
#         self.mass = mass

#     def get_radius(self):
#         return self.radius

#     def get_mass(self):
#         return self.mass

#     def get_volume(self):
#         return round((4/3 * math.pi * (self.radius**3)), 5)

#     def get_surface_area(self):
#         return round((4 * math.pi * (self.radius ** 2)), 5)

#     def get_density(self):
#         density = self.mass / self.get_volume()
#         return round(density, 5)


# ball = Sphere(2, 50)
# ball.get_radius()
# ball.get_mass()
# ball.get_volume()
# ball.get_surface_area()
# ball.get_density()


"""1.6"""


# class MyClass():
#     @classmethod
#     def class_name_changer(cls, new_name):
#         if not new_name[0].isupper() or not new_name.isalnum():
#             raise ValueError(
#                 "Invalid class name")

#         cls.__name__ = new_name


# obj = MyClass()
# MyClass.class_name_changer('newname')
# MyClass.class_name_changer('New1900')
# print(obj)
