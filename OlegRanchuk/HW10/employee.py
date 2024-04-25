class Employee:
    count = 0  

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1 

    @classmethod
    def all_employees(cls):
        print(f"Total employees: {cls.count}")

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


employee1 = Employee("Maksym Ranchuk", 100000)
employee2 = Employee("Eva Bashkirtseva", 80000)

employee1.print_info()
employee2.print_info()

Employee.all_employees()