class Human():
    def __init__(self, name) -> None:
        self.name = name

    def greetings(self):
        return f'Hello {self.name}'

    @classmethod
    def species(cls):
        return f'This is a species of Homosapiens'

    @staticmethod
    def random_message():
        return f'Random message'


person_1 = Human('Mike')

print(person_1.greetings())
print(Human.species())
print(Human.random_message())
