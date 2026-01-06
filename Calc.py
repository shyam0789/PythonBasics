class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mult(self):
        print(self.a * self.b)

calc = Calculator(8,6)
calc.add()
calc.sub()
calc.mult()