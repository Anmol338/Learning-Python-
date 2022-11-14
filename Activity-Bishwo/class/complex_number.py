class ComplexType:

    def __init__(self, real, imag):

        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}+{self.imag}j"

a = ComplexType(2,5)
print(a)
print(a.real)
print(a.imag)