from Operation import Operation

import math

class Variations(Operation):

    class Variations(Operation):

        def __init__(self, n: int, r: int, variables: list):
            while True:
                try:
                    if n <= 0 or r <= 0 or not isinstance(n, int) or not isinstance(r, int):
                        raise ValueError("n y r deben ser enteros positivos mayores y diferentes a cero.")
                    super().__init__(n, r, variables)
                    break  # Salir del bucle si la inicialización es exitosa
                except ValueError:
                    print("Error por favor intente de nuevo con números enteros mayores a cero.")
                    # Solicitar nuevamente los valores de n y r
                    n = int(input("Ingrese la cantidad de elementos (n): "))
                    r = int(input("Ingrese la cantidad de grupos (r): "))

            # Actualizar los valores de n y r en la instancia de Variations
            self.n = n
            self.r = r

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
                    result = math.factorial(self.n) / math.factorial(self.n - self.r)
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

    """
    # Ejemplo de uso:
    try:
        n = int(input("Ingrese la cantidad de elementos (n): "))
        r = int(input("Ingrese la cantidad de grupos (r): "))

        variables = []
        variations = Variations(n, r, variables)
        print("Operación ordinaria:", variations.ordinary_operation())
        print("Operación de variaciones:", variations.variation_operation())
    except ValueError:
        print("Error: Debe ingresar números enteros para n y r.")
    """
