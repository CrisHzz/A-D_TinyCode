from operation import Operation

import math


class Variations(Operation):  # O(n)
    def __init__(self):  # O(n)
        try:  # O(n)
            self.n = int(
                input(
                    "\033[96;1m" + "Ingrese la cantidad de elementos (n): " + "\033[0m"
                )
            )  # O(0)
            self.r = int(
                input("\033[96;1m" + "Ingrese la cantidad de grupos (r): " + "\033[0m")
            )  # O(0)
        except ValueError:  # O(n)
            print(
                "\033[91;1m"
                + "Error por favor intente de nuevo con números enteros positivos."
                + "\033[0m"
            )  # O(n)
            self.__init__()  # O(0)

    # Entonces la complejidad de esta parte es: 2 O(0) + 9 O(n) = O(n)

    def ordinary_operation(self):  # O(n)
        while True:  # O(n)
            try:  # O(n)
                if self.n < self.r and self.n <= 0 or self.r <= 0:  # O(n)
                    print(
                        "\033[91;1m"
                        + "n debe ser mayor o igual a r. Y n o r, entero positivo."
                        + "\033[0m"
                    )
                elif self.n < self.r:  # O(n)
                    print("\033[91;1m" + "n debe ser mayor o igual a r." + "\033[0m")
                else:
                    result = self.n**self.r  # O(n)
                    return result  # O(n)
                self.__init__()  # O(0)

            except ValueError:  # O(n)
                print(
                    "\033[91;1m"
                    + "Error por favor intente de nuevo con números enteros positivos."
                    + "\033[0m"
                )  # O(0)
                # O(0)

    # Entonces la complejidad de esta parte es: 18 O(n) = O(n)

    def variation_operation(self):  # O(n)
        while True:  # O(n)
            try:  # O(n)
                if self.n < self.r and self.n <= 0 or self.r <= 0:  # O(n)
                    print(
                        "\033[91;1m"
                        + "n debe ser mayor o igual a r. Y n o r, entero positivo."
                        + "\033[0m"
                    )
                elif self.n < self.r:  # O(n)
                    print("\033[91;1m" + "n debe ser mayor o igual a r." + "\033[0m")
                else:
                    result = math.factorial(self.n) // math.factorial(
                        self.n - self.r
                    )  # O(n)
                    return result  # O(n)
                self.__init__()  # O(0)
            except ValueError:  # O(n)
                print(
                    "\033[91;1m"
                    + "Error por favor intente de nuevo con números enteros positivos."
                    + "\033[0m"
                )  # O(n)

    # Entonces la complejidad de esta parte es: 16 O(n) = O(n)


# Entonces la complejidad total del algoritmo es: 3 O(n) = O(n)
