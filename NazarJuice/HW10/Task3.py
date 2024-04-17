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
    def print_total_employees(cls):
        """
        Print the total number of employees.
        """
        print(f"Total Employees: {cls.total_employees}")


print("Base Classes:", Employee.__base__)
print("Class Namespace:", Employee.__dict__)
print("Class Name:", Employee.__name__)
print("Module Name:", Employee.__module__)
print("Documentation:", Employee.__doc__)

emp1 = Employee("Nazar Dzhus", 70000)
emp2 = Employee("Dmytro Baluta", 60000)

emp1.display_info()
emp2.display_info()

Employee.print_total_employees()
