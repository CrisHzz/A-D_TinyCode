from operation import Operation


class Combination(Operation): # O(0)
    def __init__(self): # O(0)
        try:
            self.n = int(input("\033[96;1m" + "Ingrese la cantidad de elementos (n): " + "\033[0m")) # O(0)
            self.r = int(input("\033[96;1m" + "Ingrese la cantidad de grupos (r): " + "\033[0m")) # O(0)
        except ValueError: # O(0)
            print("\033[91;1m" + "Error por favor intente de nuevo con números enteros positivos." + "\033[0m")
        self.__init__()  # O(0)
        
    # Entonces la complejidad de esta parte es: 2 O(0) = O(0)

    def ordinary_operation(self): # O(0)
        while True: # O(0)
            try:
                if self.n < self.r and self.n <= 0 or self.r <= 0:
                    print("\033[91;1m" + "n debe ser mayor o igual a r. Y n o r, entero positivo." + "\033[0m")
                elif self.n < self.r:
                    print("\033[91;1m" + "n debe ser mayor o igual a r" + "\033[0m")
                else:
                    numerator = self.classicFactorial(self.n) # O(0)
                    denominator = self.classicFactorial(self.r) * self.classicFactorial(self.n - self.r) # O(0)
                    return numerator // denominator # O(0)
                self.__init__() # O(0)
            except ValueError: # O(0)
                print("\033[91;1m" + "Error por favor intente de nuevo con números enteros positivos." + "\033[0m")
    # Entonces la complejidad de esta parte es: 5 O(0) = O(0)

    def variation_operation(self): # O(0)
        while True:
            try:
                if self.n < self.r and self.n <= 0 or self.r <= 0:
                    print("\033[91;1m" + "n debe ser mayor o igual a r. Y n o r, entero positivo." + "\033[0m")
                elif self.n < self.r:
                    print("\033[91;1m" + "n debe ser mayor o igual a r" + "\033[0m")
                else:
                    numerator = self.classicFactorial(self.n + self.r - 1) # O(0)
                    denominator = self.classicFactorial(self.r) * self.classicFactorial(self.n - 1) # O(0)
                    return numerator // denominator # O(0)
                self.__init__() # O(0)
            except ValueError: # O(0)
                print("\033[91;1m" + "Error por favor intente de nuevo con números enteros positivos." + "\033[0m")

    # Entonces la complejidad de esta parte es: 3 O(0) = O(0)

# Entonces la complejidad total del algoritmo es: 3 O(0) =  O(0)