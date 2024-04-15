class Human:
    species = 'Homosapiens'
    
    def __init__(self,name):
        self.name = name
        
    def display_welcome_message(self):
        print(f"Hello, {self.name}! Welcome.")
    
    @classmethod
    def species_info(cls):
        return f"This is species of {cls.species}."
    
    @staticmethod
    def arbitrary_message():
        return "This is arbitrary message."
    
person1 = Human("Anna")
person1.display_welcome_message()
print(Human.species_info())
print(Human.arbitrary_message())