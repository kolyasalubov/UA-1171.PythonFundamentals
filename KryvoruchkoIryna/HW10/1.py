# # # 1

class Polygon:

    def square(self):
        pass

class Rectangle(Polygon):

    def __init__(self, length, width):
            self.length = length
            self.width = width

    def square(self):
        return self.length * self.width
    

my_rectangle = Rectangle(4, 5)
print(my_rectangle.square())

# # # 2 

class Human:

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f'Hello {self.name}!!!'

    @classmethod
    def homosapiens(cls):
        return 'It is a species of "Homosapiens"'
    
    @staticmethod
    def static_fun():
        return 'It is a static function'
    
my_human = Human('Iryna')
print(my_human.welcome_message())
print(my_human.homosapiens())
print(my_human.static_fun())

# # # 3

class Employee:

    counter = 0
    
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    def info_about_employee(self):
        print(f"{self.name} has salary {self.salary}")

    @classmethod
    def employee_counter(self):
        return Employee.counter
    
    def information():
        print("The base classes:", Employee.__base__)
        print("The class namespace:", Employee.__dict__)
        print("The class name:", Employee.__name__)
        print("The module name:", Employee.__module__)
        print("The documentation:", Employee.__doc__)   

print(f'Count = {Employee.employee_counter()}')

person_1 = Employee('Ira', 12345)
person_2 = Employee('Oleg', 23456)
person_3 = Employee('Sasha', 34567)
person_4 = Employee('Vlad', 45678)
person_5 = Employee('Polina', 56789)

print(f'Count = {Employee.employee_counter()}')

person_1.info_about_employee()
person_3.info_about_employee()
person_5.info_about_employee()

person_3.__del__()

print(f'Count = {Employee.employee_counter()}')

print(Employee.information())