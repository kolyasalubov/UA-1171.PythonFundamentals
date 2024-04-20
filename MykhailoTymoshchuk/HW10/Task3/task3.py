class Employee:
    
    """Program that will display ifo about name and salary of the employees"""
    
    total_employees = 0 #Counter for each employee
    
    def __init__(self, name, salary): #Class constructor
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
     
    @classmethod    
    def display_total_employees(cls): #classmethod and display total number of employees
        return f"Total employees is {cls.total_employees}"
    
    def information_employees(self): #Information about employees and their salary
        return f"Employee name: {self.name}\nSalary value: {self.salary}"
    
    @staticmethod #staticmethod displaying all information about employees and their salary
    def salary_info(): 
        print("Base classes: ",Employee.__bases__)
        print("Class namespace: ", Employee.__dict__)
        print("Class name: ", Employee.__name__)
        print("Module name: ", Employee.__module__)
        print("Documentation bar: ", Employee.__doc__)
        
#Some Eployees class exemple
emp1 = Employee("Morgan", 60000)
emp2 = Employee("Sahra", 35000)

#Display total informating about employees
print(emp1.information_employees())
print(emp2.information_employees())
#Display total total value of employees
print(Employee.display_total_employees())
Employee.salary_info
