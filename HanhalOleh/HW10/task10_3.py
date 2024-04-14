class Employee:
    """
    class: Employee
    obj params: str name, int salary
    """
    total_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
    
    @classmethod
    def display_total_employees(self):
        return f"Number of employees: {self.total_employees}"

    def employee_info(self):
        return f"Name: {self.name}\nSalary: {self.salary}\n"
    
    @staticmethod
    def add_info():
        print("Base classes:", Employee.__base__)
        print("Namespace:", Employee.__dict__)
        print("Class name:", Employee.__name__)
        print("Module name:", Employee.__module__)
        print("Documentation:", Employee.__doc__)

########## Example usage ##########

empl1 = Employee("John", 35000)
empl2 = Employee("Max", 40000)
empl3 = Employee("Harry", 37000)

print(empl1.employee_info())
print(empl2.employee_info())
print(empl3.employee_info())

print(Employee.display_total_employees())
print(Employee.add_info())


    


    
