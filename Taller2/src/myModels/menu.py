import sys

sys.path.append("/home/kalichhe/Desktop/A-D_TinyCode/Taller2/src/myModels")

from colorama import init

init()

from permutation import Permutation
from combinations import Combination
from varations import Variations
from principlesCounting import PrinciplesCounting


class Menu:  # O(n)
    def __init__(self):  # O(n)
        while True:  # O(n)
            try:
                self.decision = int(
                    input(
                        "\033[93;1m"
                        + "\nSelecciona \n(1) Técnicas de conteo \n(2) Técnicas de combinatorias \n(3) Para salir \nopción: "
                        + "\033[0m"
                    )
                )  # O(n)
                if self.decision == 3:  # O(n)
                    break  # O(n)
                elif self.decision == 2:  # O(n)
                    while True:  # O(n)
                        try:
                            self.decision = int(
                                input(
                                    "\033[94;1m"
                                    + "\n\t¿Importa el orden? \n\t(1) Si \n\t(2) No \n\tOpción: "
                                    + "\033[0m"
                                )
                            )  # O(n)
                            if self.decision == 1 or self.decision == 2:  # O(n)
                                break  # O(n)
                            else:  # O(n)
                                print(
                                    "\033\t[91;1m" + "Opción no válida" + "\033[0m"
                                )  # O(n)
                        except ValueError:
                            print(
                                "\033\t[91;1m"
                                + "Solo se permiten números, positivos"
                                + "\033[0m"
                            )
                    if self.decision == 1:  # O(n)
                        while True:  # O(n)
                            try:
                                self.decision = int(
                                    input(
                                        "\033[95;1m"
                                        + "\n\t\t¿Intervienen todos los elementos? \n\t\t(1) Si \n\t\t(2) No \n\t\tOpción: "
                                        + "\033[0m"
                                    )
                                )  # O(n)
                                if self.decision == 1 or self.decision == 2:  # O(n)
                                    break  # O(n)
                                else:  # O(n)
                                    print(
                                        "\033[91;1m" + "Opción no válida" + "\033[0m"
                                    )  # O(n)
                            except ValueError:
                                print(
                                    "\033[91;1m"
                                    + "Solo se permiten números, positivos"
                                    + "\033[0m"
                                )
                        if self.decision == 2:  # O(n)
                            while True:  # O(n)
                                try:
                                    self.decision = int(
                                        input(
                                            "\033[92;1m"
                                            + "\n\t\t\t¿Se repiten los elementos? \n\t\t\t(1) Si \n\t\t\t(2) No \n\t\t\topción: "
                                            + "\033[0m"
                                        )
                                    )  # O(n)
                                    if self.decision == 1 or self.decision == 2:  # O(n)
                                        break  # O(n)
                                    else:  # O(n)
                                        print(
                                            "\033[91;1m"
                                            + "Opción no válida"
                                            + "\033[0m"
                                        )  # O(n)
                                except ValueError:
                                    print(
                                        "\033[91;1m"
                                        + "Solo se permiten números, positivos"
                                        + "\033[0m"
                                    )
                            if self.decision == 2:  # O(n)
                                print(
                                    "\033[97;1m" + "\nVariations ordinary" + "\033[0m"
                                )  # O(n)
                                operation = Variations()  # O(n)
                                print(
                                    "\033[92;1m"
                                    + str(operation.ordinary_operation())
                                    + "\033[0m"
                                )  # O(n)
                            else:  # O(n)
                                print(
                                    "\033[97;1m"
                                    + "\nVariations with repetitions"
                                    + "\033[0m"
                                )  # O(n)
                                operation = Variations()  # O(n)
                                print(
                                    "\033[92;1m"
                                    + str(operation.variation_operation())
                                    + "\033[0m"
                                )  # O(n)
                        else:  # O(n)
                            while True:  # O(n)
                                self.decision = int(
                                    input(
                                        "\033[92;1m"
                                        + "\n\t\t\t¿¿Se repiten los elementos? \n\t\t\t(1) Si \n\t\t\t(2) No \n\t\t\topción: "
                                        + "\033[0m"
                                    )
                                )  # O(n)
                                if self.decision == 1 or self.decision == 2:  # O(n)
                                    break  # O(n)
                                else:  # O(n)
                                    print(
                                        "\033[91;1m" + "Opción no válida" + "\033[0m"
                                    )  # O(n)
                            if self.decision == 2:  # O(n)
                                print(
                                    "\033[97;1m" + "\nPermutations ordinary" + "\033[0m"
                                )  # O(n)
                                operation = Permutation()  # O(n)
                                print(
                                    "\033[92;1m"
                                    + str(operation.ordinary_operation())
                                    + "\033[0m"
                                )  # O(n)
                            else:  # O(n)
                                print(
                                    "\033[97;1m"
                                    + "\nPermutations with repetitions"
                                    + "\033[0m"
                                )  # O(n)
                                operation = Permutation()  # O(n)
                                print(
                                    "\033[92;1m"
                                    + str(operation.variation_operation())
                                    + "\033[0m"
                                )  # O(n)
                    else:  # O(n)
                        while True:  # O(n)
                            try:
                                self.decision = int(
                                    input(
                                        "\033[92;1m"
                                        + "\n\t\t¿Se repiten los elementos? \n\t\t(1) Si \n\t\t(2) No \n\t\topción: "
                                        + "\033[0m"
                                    )
                                )  # O(n)
                                if self.decision == 1 or self.decision == 2:  # O(n)
                                    break  # O(n)
                                else:  # O(n)
                                    print(
                                        "\033[91;1m" + "Opción no válida" + "\033[0m"
                                    )  # O(n)
                            except ValueError:
                                print(
                                    "\033[91;1m"
                                    + "Solo se permiten números, positivos"
                                    + "\033[0m"
                                )
                        if self.decision == 2:  # O(n)
                            print(
                                "\033[97;1m" + "\nCombinations ordinary" + "\033[0m"
                            )  # O(n)
                            operation = Combination()  # O(n)
                            print(
                                "\033[92;1m"
                                + str(operation.ordinary_operation())
                                + "\033[0m"
                            )  # O(n)
                        else:  # O(n)
                            print(
                                "\033[97;1m"
                                + "\nCombinations with repetitions"
                                + "\033[0m"
                            )  # O(n)
                            operation = Combination()  # O(n)
                            print(
                                "\033[92;1m"
                                + str(operation.variation_operation())
                                + "\033[0m"
                            )  # O(n)
                elif self.decision == 1:  # O(n)
                    operation = PrinciplesCounting()  # O(n)
                    print("\033[97;1m" + "\nPrinciples of counting" + "\033[0m")  # O(n)
                    print(
                        "\033[92;1m" + str(operation.list_multiplier()) + "\033[0m"
                    )  # O(n)
                else:  # O(n)
                    print("\033[91;1m" + "Opción no válida" + "\033[0m")  # O(n)
            except ValueError:
                print(
                    "\033[91;1m" + "Solo se permiten números, positivos" + "\033[0m"
                )  # O(n)

    # Entonces la complejidad de esta parte es: 43 O(n) = O(n)


# Entonces la complejidad total del algoritmo es: 1 O(0) + 1 O(n) = O(n)
