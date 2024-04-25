class Employee:
    """This is an Employee class. It stores employees' names and salaries.
    """
    amount_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.amount_of_employees += 1

    @classmethod
    def print_amount_of_employees(c):
        print(f"Total amount of employees: {c.amount_of_employees}\n")

    def employee_info(self):
        print(f"{self.name} has {self.salary} as monthly salary.")
