class Human:

    def __init__(self, name):
        self.name = str(name)
    
    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def scpecies(cls):
        return "Homosapiens."
    
    @staticmethod
    def message():
        return "Some text.\n"
    
    # I added all needed methods in one that can simply call them all in one turn
    # so our main file is more clear

    def info(self):
        print(self.welcome())
        print(self.scpecies())
        print(self.message())