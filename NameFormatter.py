class NameFormatter:

    def __init__(self,name):
        self.name = name

    def print_name(self):
        print(f"Welcome Mr/Mrs. {self.name}!")


name = NameFormatter("Shyam Sundar")
name.print_name()
