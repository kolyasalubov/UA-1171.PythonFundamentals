from pprint import pprint
from class_Employee import Employee

first_employee = Employee("Maria", 4000)
second_employee = Employee("Anna", 4700)
third_employee = Employee("Max", 3300)

Employee.print_amount_of_employees()

first_employee.employee_info()
second_employee.employee_info()
third_employee.employee_info()


print("\nClass Name:", Employee.__name__)
print("Namespace:")
pprint(Employee.__dict__)
print("Module Name:", Employee.__module__)
print("Base classes for Employee:", Employee.__base__)
print("Documentation:", Employee.__doc__)
