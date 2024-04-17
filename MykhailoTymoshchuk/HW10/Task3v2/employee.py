class Employee:
    
    total_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
     
    @classmethod    
    def display_total_employees(cls):
        return f"Total employees is {cls.total_employees}"
    
    def information_employees(self):
        return f"Employee name: {self.name}\nSalary value: {self.salary}"
    
    @staticmethod
    def salary_info():
        print("Base classes: ",Employee.__bases__)
        print("Class namespace: ", Employee.__dict__)
        print("Class name: ", Employee.__name__)
        print("Module name: ", Employee.__module__)
        print("Documentation bar: ", Employee.__doc__)