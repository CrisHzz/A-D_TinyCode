from Operation import Operation


class Combination(Operation):
    def __init__(self):
        self.n = int(input("Ingrese la cantidad de elementos (n): "))
        self.r = int(input("Ingrese la cantidad de grupos (r): "))

    def ordinary_operation(self):
        if self.n < self.r:
            raise ValueError("El valor de n debe ser mayor o igual que r")

        numerator = self.classicFactorial(self.n)
        denominator = self.classicFactorial(self.r) * self.classicFactorial(
            self.n - self.r
        )

        return numerator // denominator

    def variation_operation(self):
        numerator = self.classicFactorial(self.n + self.r - 1)
        denominator = self.classicFactorial(self.r) * self.classicFactorial(self.n - 1)

        return numerator // denominator
