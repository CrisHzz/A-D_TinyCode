from abc import ABC, abstractmethod

import math

class Operation(ABC): # O(n^3)
    def __init__(self,n:int,r:int,variables:list): # O(0)
        self.n=n # O(0)
        self.r=r # O(0)
        self.variables=variables # O(0)
    # Entonces la complejidad de esta parte es: 3 O(0) = O(0)

    def classicFactorial(self, n: int): # O(0)
        if not isinstance(n, int): # O(0)
            raise ValueError("Tiene que ser entero") # O(0)
        if n < 0: # O(0)
            raise ValueError("Positivo porfavor!") # O(0)
        return math.factorial(n) # O(0)
    # Entonces la complejidad de esta parte es: 5 O(0) = O(0)
    
    def find_variables(self): # O(n)
        while True: # O(n)
            try: # O(n)
                num_variables = int(input("Porfavor ingrese el numero de variables: ")) # O(n)
                self.variables = [] # O(n)
                for i in range(num_variables): # O(n^2)
                    while True: # O(n^3)
                        try: # O(n^3)
                            variable = int(input(f"Ingrese la variable N°{i+1}: ")) # O(n^3)
                            self.variables.append(variable) # O(n^3)
                            break  # O(n^3)
                        except ValueError: # O(n^3)
                            print("Error: Tienes que digitar un natural para la variable.") # O(n^3)
                            continue # O(n^3)
                break # O(n)
            except ValueError: # O(n)
                print("Numero incorrecto, sigue intentado") # O(n)
    # Entonces la complejidad de esta parte es: 7 O(n) + 1 O(n^2) + 8 O(n^3) = O(n^3)

    @abstractmethod # O(0)
    def ordinary_operation(self): # O(0)
        pass # O(0)
    # Entonces la complejidad de esta parte es: 1 O(0)
    
    @abstractmethod # O(0)
    def variation_operation(self): # O(0)
        pass # O(0)
    # Entonces la complejidad de esta parte es: 1 O(0)
    
# Entonces la complejidad total del algoritmo es: 6 O(0) + 1 O(n^3) = O(n^3)