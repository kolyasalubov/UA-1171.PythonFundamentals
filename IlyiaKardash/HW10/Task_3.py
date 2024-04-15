class Employee():
    number_of_employees = 0

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employee.number_of_employees += 1

    @classmethod
    def numb_of_employees(self):
        return f'Total number of employees is {self.number_of_employees}'

    def info_about_employee(self):
        return f'Employee name is: {self.name} with a salary of {self.salary}'

    @staticmethod
    def information():
        print("Base classes:", Employee.__base__)
        print("Namespace:", Employee.__dict__)
        print("Class name:", Employee.__name__)
        print("Module name:", Employee.__module__)
        print("Documentation:", Employee.__doc__)


employee_1 = Employee('John', 5000)
employee_2 = Employee('David', 7000)
employee_3 = Employee('Mike', 15000)

print(employee_1.info_about_employee())
print(employee_2.info_about_employee())
print(employee_3.info_about_employee())

print(Employee.numb_of_employees())
print(Employee.information())
