class Human: 
    def __init__(self, name):
        self.name = name 

    def hello(self):
        print(f"Hello {self.name}")

    @classmethod
    def about_species(cls):
        return "Homosapiens"

    @staticmethod
    def get_massage():
        return "An arbitrary massage"
    
human = Human("Eva")
human.hello()
species = Human.about_species()
print(f"Human species {species}")
static_massage = Human.get_massage()
print(static_massage)