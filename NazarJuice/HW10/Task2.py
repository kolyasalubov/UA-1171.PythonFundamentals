class Human():
    def __init__(self, name):
        self.name = name
    
    def welcome(self):
        return f'Hello {self.name}'
    
    @classmethod
    def species(cls):
        return f'spcies: Homosapiens'
    
    @staticmethod
    def message():
        return f'message'

Adam = Human('Adam')
    
print(Adam.welcome())
print(Human.species())
print(Human.message())