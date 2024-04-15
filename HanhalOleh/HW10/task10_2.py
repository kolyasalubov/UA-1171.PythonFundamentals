class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, {self.name}!"

    @classmethod
    def species_info(cls):
        return "This is a species of Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary print from static method"
    
############## Example usage ##############

person1 = Human("John")

print(person1.welcome())
print(Human.species_info())
print(Human.arbitrary_message())
