class Employee:
    employees_count = 0
    # I added the list of objects inside the class 
    # so it will look like database (or something like it)
    emp_list = []

    def __init__(self, name, salary):
        Employee.employees_count+=1
        self.name = name
        self.salary = salary
        Employee.emp_list.append([self.name, self.salary])

    def __del__(self):
        Employee.employees_count-=1
        Employee.emp_list.remove([self.name, self.salary])
        print(f"Removing employee {self.name}")

    def total_employees(cls):
        print(f"Total count: {Employee.employees_count}.")
        for i in range(Employee.employees_count):
            print(f"{Employee.emp_list[i][0]}, {Employee.emp_list[i][1]} $")
        print('\n')

    def details(self):
        print(f"Name: {self.name}.\nSalary: {self.salary} $.\n")

    def class_info(cls):
        print(f"The base classes: {Employee.__base__}\n")
        print(f"\nThe class namespace: {Employee.__dict__}\n")
        print(f"\nThe class name: {Employee.__name__}\n")
        print(f"\nThe module name: {Employee.__module__}\n")
        print(f"\nThe documentation bar: {Employee.__doc__}\n")
