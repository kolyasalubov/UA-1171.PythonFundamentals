class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome {self.name}!"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def arbitrary_message():
        return "Static method"



person1 = Human("Alice")
person2 = Human("Bob")
print(person1.welcome_message())
print(person2.welcome_message())
print(Human.get_species())
print(Human.arbitrary_message())
