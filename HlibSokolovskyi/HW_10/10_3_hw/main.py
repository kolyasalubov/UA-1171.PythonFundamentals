from employee_class import *

emp1 = Employee("John", 900)
emp2 = Employee("Alice", 1110)
emp2.total_employees()

emp3 = Employee("Emily", 1500)
emp3.total_employees()


emp1.details()
emp2.details()
emp3.details()

del emp1
emp3.total_employees()

emp3.class_info()
