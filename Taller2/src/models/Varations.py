from Operation import Operation

import math


class Variations(Operation):

        def __init__(self):
            self.n = int(input("Ingrese la cantidad de elementos (n): "))
            self.r = int(input("Ingrese la cantidad de grupos (r): "))
            while True:
                try:
                    if self.n <= 0 or self.r <= 0 or not isinstance(self.n, int) or not isinstance(self.r, int):
                        raise ValueError("n y r deben ser enteros positivos mayores y diferentes a cero.")
                    # super().__init__(n, r, variables)
                    break  # Salir del bucle si la inicialización es exitosa
                except ValueError:
                    print("Error por favor intente de nuevo con números enteros mayores a cero.")
                    # Solicitar nuevamente los valores de n y r
                    self.n = int(input("Ingrese la cantidad de elementos (n): "))
                    self.r = int(input("Ingrese la cantidad de grupos (r): "))

        def ordinary_operation(self):
            while True:
                try:
                    if self.n == 0 or self.r == 0:
                        raise ValueError("n y r deben ser números enteros mayores a cero.")
                    result = self.n ** self.r
                    return result
                except ValueError as e:
                    print("Error:", e)
                    # Solicitar nuevamente los valores de n y r
                    n = int(input("Ingrese la cantidad de elementos (n): "))
                    r = int(input("Ingrese la cantidad de grupos (r): "))
                    # Actualizar los valores de n y r en la instancia de Variations
                    self.n = n
                    self.r = r
                except TypeError:
                    print("Error: n y r deben ser números enteros.")
                    # Solicitar nuevamente los valores de n y r
                    n = int(input("Ingrese la cantidad de elementos (n): "))
                    r = int(input("Ingrese la cantidad de grupos (r): "))
                    # Actualizar los valores de n y r en la instancia de Variations
                    self.n = n
                    self.r = r

        def variation_operation(self):
            while True:
                try:
                    result = math.factorial(self.n) // math.factorial(self.n - self.r)
                    return result
                except ValueError:
                    print("Error por favor intente de nuevo con números enteros mayores a cero.")
                    # Solicitar nuevamente los valores de n y r
                    n = int(input("Ingrese la cantidad de elementos (n): "))
                    r = int(input("Ingrese la cantidad de grupos (r): "))
                    # Actualizar los valores de n y r en la instancia de Variations
                    self.n = n
                    self.r = r
                except TypeError:
                    print("Error: n y r deben ser números enteros.")
                    # Solicitar nuevamente los valores de n y r
                    n = int(input("Ingrese la cantidad de elementos (n): "))
                    r = int(input("Ingrese la cantidad de grupos (r): "))
                    # Actualizar los valores de n y r en la instancia de Variations
                    self.n = n
                    self.r = r