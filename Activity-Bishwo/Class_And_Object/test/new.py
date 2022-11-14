class Calculator:

    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    # #For user
    # def __str__(self):
    #     return "Calc is  object of Calculator\nABC"

    # # For developer
    # def __repr__(self):
    #     return r"Calc is  object of Calculator\nABC"

    def calculator(self):
        match self.op:
            case '+':
                self.add()
            case '-':
                self.sub()
            case '*':
                self.mul()

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

# calc = Calculator(10, 20, '-')
# print(calc)
# print(str(calc))
# print(repr(calc))

calc = Calculator(10, 20, '+')
print(calc.add())

calc_diff = Calculator(20, 10, '-')
print(calc_diff.sub())

calc_pro = Calculator(20, 10, '*')
print(calc_pro.mul())