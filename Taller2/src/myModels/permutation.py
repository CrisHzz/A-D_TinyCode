from operation import Operation


class Permutation(Operation): # O(n)
    def __init__(self,): # O(0)
        self.n = int(input("\033[96;1m" + "Ingrese la cantidad de elementos (n): " + "\033[0m")) # O(0)
        self.r = int(input("\033[96;1m" + "Ingrese la cantidad de grupos (r): " + "\033[0m")) # O(0)
        self.variables = [] # O(0)
    # Entonces la complejidad de esta parte es: 3 O(0) = O(0)
    
    def circular_permutation(self): # O(0)
        if not isinstance(self.n, int): # O(0)
            raise ValueError("\033[91;1m" + "Tiene que ser un entero" + "\033[0m") # O(0)
        if self.n < 0: # O(0)
            raise ValueError("\033[91;1m" + "Tiene que ser un positivo" + "\033[0m") # O(0)
        return self.classicFactorial(self.n) - 1 # O(0)
    # Entonces la complejidad de esta parte es: 5 O(0) = O(0)

    def ordinary_operation(self): # O(0)
        if not isinstance(self.n, int) or not isinstance(self.r, int): # O(0)
            raise ValueError("\033[91;1m" + "Tiene que ser un entero" + "\033[0m") # O(0)
        if self.n < 0 or self.r < 0: # O(0)
            raise ValueError("\033[91;1m" + "Tiene que ser un positivo" + "\033[0m") # O(0)
        return self.classicFactorial(self.n) // self.classicFactorial(self.n - self.r) # O(0)
    # Entonces la complejidad de esta parte es: 5 O(0) = O(0)

    # Entonces la complejidad de esta parte es: 3 O(0) = O(0)
    
    def variation_operation(self): # O(n)
        if not isinstance(self.n, int) or not isinstance(self.r, int): # O(0)
            raise ValueError("\033[91;1m" + "Tiene que ser un entero" + "\033[0m") # O(0)
        if self.n <= self.r: # O(0)
            raise ValueError("\033[91;1m" + "n tiene que ser mayor que r" + "\033[0m") # O(0)
        if self.n < 0: # O(0)
            raise ValueError("\033[91;1m" + "Tiene que ser un positivo" + "\033[0m") # O(0)
        numerator = self.classicFactorial(self.n) # O(0)
        denominator = 1 # O(0)
        for variable in self.variables: # O(n)
            denominator *= self.classicFactorial(variable) # O(n)
        return numerator // denominator # O(0)
    # Entonces la complejidad de esta parte es: 9 O(0) + 2 O(n) = O(n)
    
# Entonces la complejidad total del algoritmo es: 3 O(0) + 1 O(n) = O(n)
