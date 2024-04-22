class Human:
    def __init__(self, name):
        self.name = name
        self.species = "Homo sapiens"

    def welcome(self):
        print(f"Hello, {self.name}! Welcome!")

    def check_species(self):
        print(f"{self.name} is a human, and human's species is a {self.species}.")

    @staticmethod
    def message():
        print("This is the message.")
