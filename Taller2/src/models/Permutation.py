from Operation import Operation


class Permutation(Operation):
    def __init__(self):
        self.n = int(input("Ingrese la cantidad de elementos (n): "))
        self.r = int(input("Ingrese la cantidad de grupos (r): "))

    def circular_permutation(self):
        if not isinstance(self.n, int):  # Verificamos los casos de excepciones
            raise ValueError("Tiene que ser un entero")
        if self.n < 0:
            raise ValueError("Tiene que ser un positivo")
        return self.classicFactorial(self.n) - 1  # Formula de permutacion circular n-1

    def ordinary_operation(self):
        if not isinstance(self.n, int) or not isinstance(self.r, int):
            raise ValueError("Tiene que ser un entero")
        if self.n < 0 or self.r < 0:
            raise ValueError("Tiene que ser un positivo")

        return self.classicFactorial(self.n) // self.classicFactorial(
            self.n - self.r
        )  # Formula de permutacion ordinaria n!/(n-r)!

    def variation_operation(self):
        if not isinstance(self.n, int) or not isinstance(self.r, int):
            raise ValueError("Tiene que ser un entero")
        
        if self.n <= self.r:
            raise ValueError("n tiene que ser mayor que r")
                
        if self.n < 0:
            raise ValueError("Tiene que ser un positivo")

        numerator = self.classicFactorial(self.n)  # Numerador n

        denominator = 1

        for (variable) in (self.variables):  # Denominador es las permutaciones de cada una de las variables independientes

            denominator *= self.classicFactorial(variable)

        return numerator // denominator  # Numerador divido denominador
