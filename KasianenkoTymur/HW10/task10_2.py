from random import randint

class Human():
    def __init__(self, name):
        self.name = name
    def welcome_message(self):
        return f'Hello, {self.name}!'
    
    @classmethod
    def species(clas):
        return f'Spcies: Homosapiens'
    @staticmethod
    def message():
        return f'Arbitrary message.'

while True:
    names=['Tymur', 'Victor','Svitlana', 'Alex', 'Vadym']
    person = Human(names[randint(0,4)])
        
    print(person.welcome_message())
    print(Human.species())
    print(Human.message())

    answer=input('Try again? (y/n)\n')
    if answer=='n':
        break