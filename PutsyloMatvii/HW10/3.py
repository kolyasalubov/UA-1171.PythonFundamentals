class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total employees: {cls.total_employees}")



print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp1.display_info()
emp2.display_info()
Employee.display_total_employees()
