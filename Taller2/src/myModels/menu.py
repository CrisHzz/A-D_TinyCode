import sys
sys.path.append("/home/kalichhe/Desktop/A-D_TinyCode/Taller2/src/myModels")

from permutation import Permutation
from combinations import Combination
from varations import Variations
from principlesCounting import PrinciplesCounting


class Menu():  # O(n)
    def __init__(self):  # O(n)
        while True:  # O(n)
            self.decision = int(
                input(
                    "\nSelecciona \n(1) Técnicas de conteo \n(2) Técnicas de combinatorias \n(3) Para salir \nopción: "
                )
            )  # O(n)
            if self.decision == 3:  # O(n)
                break  # O(n)
            elif self.decision == 2:  # O(n)
                self.decision = int(
                    input("\n\t¿Importa el orden? \n\t(1) Si \n\t(2) No \n\tOpción: ")
                )  # O(n)
                if self.decision == 1:  # O(n)
                    self.decision = int(
                        input(
                            "\n\t\t¿Intervienen todos los elementos? \n\t\t(1) Si \n\t\t(2) No \n\t\tOpción: "
                        )
                    )  # O(n)
                    if self.decision == 2:  # O(n)
                        self.decision = int(
                            input(
                                "\n\t\t\t¿Se repiten los elementos? \n\t\t\t(1) Si \n\t\t\t(2) No \n\t\t\topción: "
                            )
                        )  # O(n)
                        if self.decision == 2:  # O(n)
                            print("\nVariations ordinary")  # O(n)
                            operation = Variations()  # O(n)
                            print(operation.ordinary_operation())  # O(n)
                        else:  # O(n)
                            print("\nVariations with repetitions")  # O(n)
                            operation = Variations()  # O(n)
                            print(operation.variation_operation())  # O(n)
                    else:  # O(n)
                        self.decision = int(
                            input(
                                "\n\t\t\t¿¿Se repiten los elementos? \n\t\t\t(1) Si \n\t\t\t(2) No \n\t\t\topción: "
                            )
                        )  # O(n)
                        if self.decision == 2:  # O(n)
                            print("\nPermutations ordinary")  # O(n)
                            operation = Permutation()  # O(n)
                            print(operation.ordinary_operation())  # O(n)
                        else:  # O(n)
                            print("\nPermutations with repetitions")  # O(n)
                            operation = Permutation()  # O(n)
                            print(operation.variation_operation())  # O(n)
                else:  # O(n)
                    self.decision = int(
                        input(
                            "\n\t\t¿Se repiten los elementos? \n\t\t(1) Si \n\t\t(2) No \n\t\topción: "
                        )
                    )  # O(n)
                    if self.decision == 2:  # O(n)
                        print("\nCombinations ordinary")  # O(n)
                        operation = Combination()  # O(n)
                        print(operation.ordinary_operation())  # O(n)
                    else:  # O(n)
                        print("\nCombinations with repetitions")  # O(n)
                        operation = Combination()  # O(n)
                        print(operation.variation_operation())  # O(n)
            else:  # O(n)
                operation = PrinciplesCounting()  # O(n)
                print(operation.list_multiplier())  # O(n)

    # Entonces la complejidad de esta parte es: 41 O(n) = O(n)

# Entonces la complejidad total del algoritmo es: 1 O(0) + 1 O(n) = O(n)
