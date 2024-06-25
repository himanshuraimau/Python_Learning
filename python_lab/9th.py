class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    @staticmethod
    def addi(c1,c2):
        temp = Complex(0, 0)
        temp.real = c1.real + c2.real
        temp.imaginary= c1.imaginary + c2.imaginary
        return temp 

c1 = Complex(2, 3)
c2 = Complex(1, 2)
c3 = Complex.addi(c1,c2)
print("Real part:", c3.real,"+i",str(c3.imaginary))