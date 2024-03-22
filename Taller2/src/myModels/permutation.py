from operation import Operation


class Permutation(Operation):  # O(n)
    def __init__(self):  # O(0)
        try:  # O(0)
            self.n = int(
                input(
                    "\033[96;1m" + "Ingrese la cantidad de elementos (n): " + "\033[0m"
                )
            )  # O(0)
            self.r = int(
                input("\033[96;1m" + "Ingrese la cantidad de grupos (r): " + "\033[0m")
            )  # O(0)
            self.variables = []  # O(0)
        except ValueError:
            print(
                "\033[91;1m"
                + "Error por favor intente de nuevo con números enteros positivos."
                + "\033[0m"
            )
            self.__init__()  # O(0)
            

    # Entonces la complejidad de esta parte es: 3 O(0) = O(0)

    def circular_permutation(self):  # O(0)
        while True:  # O(0)
            try:  # O(0)
                if self.n <= 0:
                    print("\033[91;1m" + "n entero positivo." + "\033[0m")
                else:
                    return self.classicFactorial(self.n) - 1  # O(0)
            except ValueError:  # O(0)
                print(
                    "\033[91;1m"
                    + "Error por favor intente de nuevo con números enteros positivos."
                    + "\033[0m"
                )  # O(0)

    # Entonces la complejidad de esta parte es: 5 O(0) = O(0)

    def ordinary_operation(self):  # O(0)
        while True:  # O(0)
            try:
                if self.n < self.r and self.n <= 0 or self.r <= 0:  # O(n)
                    print(
                        "\033[91;1m"
                        + "n debe ser mayor o igual a r. Y n o r, entero positivo."
                        + "\033[0m"
                    )
                elif self.n < self.r:  # O(n)
                    print("\033[91;1m" + "n debe ser mayor o igual a r." + "\033[0m")
                else:
                    return self.classicFactorial(self.n) // self.classicFactorial(
                        self.n - self.r
                    )  # O(0)
                self.__init__()  # O(0)

            except ValueError:  # O(0)
                print(
                    "\033[91;1m"
                    + "Error por favor intente de nuevo con números enteros positivos."
                    + "\033[0m"
                )  # O(0)

    # Entonces la complejidad de esta parte es: 3 O(0) = O(0)

    def variation_operation(self):  # O(n)
        try:
            if self.n < self.r and self.n <= 0 or self.r <= 0:  # O(n)
                print(
                    "\033[91;1m"
                    + "n debe ser mayor o igual a r. Y n o r, entero positivo."
                    + "\033[0m"
                )
            elif self.n < self.r:  # O(n)
                print("\033[91;1m" + "n debe ser mayor o igual a r." + "\033[0m")
            else:
                numerator = self.classicFactorial(self.n)  # O(0)
                denominator = 1  # O(0)
                for variable in self.variables:  # O(n)
                    denominator *= self.classicFactorial(variable)  # O(n)
                return numerator // denominator  # O(0)
            self.__init__()  # O(0)
        except ValueError:  # O(n)
            print(
                "\033[91;1m"
                + "Error por favor intente de nuevo con números enteros positivos."
                + "\033[0m"
            )

    # Entonces la complejidad de esta parte es: 9 O(0) + 2 O(n) = O(n)


# Entonces la complejidad total del algoritmo es: 3 O(0) + 1 O(n) = O(n)
