class PrinciplesCounting(list):  # O(0)
    def __init__(self):  # O(0)
        try:  # O(0)
            input_value = input(
                "\033[96;1m"
                + "\nIngrese los valores separados por espacios: "
                + "\033[0m"
            )  # O(0)
            values = map(int, input_value.split())  # O(n)
            if input_value == "":
                raise ValueError(
                    "\033[91;1m" + "Debe ingresar al menos un número entero positivo." + "\033[0m"
                )
            if any(value <= 0 or isinstance(value, str) for value in values):  # O(n)
                raise ValueError(
                    "\033[96;1m"
                    + "Debe ingresar solo números enteros positivos diferentes de cero."
                    + "\033[0m"
                )  # O(n)
            super().__init__(map(int, input_value.split()))  # O(n)
        except ValueError:  # O(0)
            print(
                "\033[91;1m" + "Error por favor digite un numero entero positivo :)" + "\033[0m"
            )  # O(0)
            self.__init__()  # O(0)

    # Entonces la complejidad de esta parte es: 9 O(0) = O(0)

    def list_multiplier(self):  # O(n)
        result = 1  # O(0)
        for value in self:  # O(n)
            result *= value  # O(n)
        return result  # O(0)

    # Entonces la complejidad de esta parte es: 2 O(0) + 2 O(n) = O(n)


# Entonces la complejidad total del algoritmo es: 1 O(0) + 1 O(n) = O(n)
