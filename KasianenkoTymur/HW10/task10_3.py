from random import randint

class Employee:
    """
    Employee class represents an employee with name and salary attributes.
    """
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        """
        Display information about the employee's name and salary.
        """
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def print_total_employees(clas):
        """
        Print the total number of employees.
        """
        print(f"Total Employees: {clas.total_employees}")


print("Base Classes:", Employee.__base__)
print("Class Namespace:", Employee.__dict__)
print("Class Name:", Employee.__name__)
print("Module Name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

name=['Tymur', 'Victor','Svitlana', 'Alex', 'Vadym']
last_name=['Gerard', 'Edison', 'Sydney', 'Hesketh', 'De Benoist']
salary=[57846, 18965, 86502, 40068, 37942]

for i in range(randint(0,4)):
    employee = Employee(f'{last_name[randint(0,4)]} {name[randint(0,4)]}', salary[i])
    employee.display_info()

Employee.print_total_employees()