class NameFormatter:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def welcome(self):
        print(f"Welcome Mr/Mrs. {self.name}!")
    def print_age(self):
        print(f"You are {self.age} years old.")


name = NameFormatter("Shyam Sundar",36)
name.welcome()
name.print_age()
