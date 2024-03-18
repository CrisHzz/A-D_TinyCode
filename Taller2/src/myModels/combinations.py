from operation import Operation


class Combination(Operation): # O(0)
    def __init__(self): # O(0)
        self.n = int(input("\033[96;1m" + "Ingrese la cantidad de elementos (n): " + "\033[0m")) # O(0)
        self.r = int(input("\033[96;1m" + "Ingrese la cantidad de grupos (r): " + "\033[0m")) # O(0)
    # Entonces la complejidad de esta parte es: 2 O(0) = O(0)

    def ordinary_operation(self): # O(0)
        if self.n < self.r: # O(0)
            raise ValueError("\033[91;1m" + "El valor de n debe ser mayor o igual que r" + "\033[0m") # O(0)

        numerator = self.classicFactorial(self.n) # O(0)
        denominator = self.classicFactorial(self.r) * self.classicFactorial(self.n - self.r) # O(0)

        return numerator // denominator # O(0)
    # Entonces la complejidad de esta parte es: 5 O(0) = O(0)

    def variation_operation(self): # O(0)
        numerator = self.classicFactorial(self.n + self.r - 1) # O(0)
        denominator = self.classicFactorial(self.r) * self.classicFactorial(self.n - 1) # O(0)

        return numerator // denominator # O(0)
    # Entonces la complejidad de esta parte es: 3 O(0) = O(0)

# Entonces la complejidad total del algoritmo es: 3 O(0) =  O(0)