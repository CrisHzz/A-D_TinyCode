from Permutation import Permutation
from Combinations import Combination
from Varations import Variations
from PrinciplesCounting import PrinciplesCounting


class Menu:
    def __init__(self):
        while True:
            self.decision = int(
                input(
                    "Selecciona \n(1) Técnicas de conteo \n(2) Técnicas de combinatorias \n(3) Para salir \nopción: "
                )
            )
            if self.decision == 3:
                break
            elif self.decision == 2:
                self.decision = int(
                    input("\t¿Importa el orden? \n\t(1) Si \n\t(2) No \n\tOpción: ")
                )
                if self.decision == 1:
                    self.decision = int(
                        input(
                            "\t\t¿Intervienen todos los elementos? \n\t\t(1) Si \n\t\t(2) No \n\t\tOpción: "
                        )
                    )
                    if self.decision == 2:
                        self.decision = int(
                            input(
                                "\t\t\t¿Se repiten los elementos? \n\t\t\t(1) Si \n\t\t\t(2) No \n\t\t\topción: "
                            )
                        )
                        if self.decision == 2:
                            print("Variations ordinary")
                            operation = Variations()
                            print(operation.ordinary_operation())
                        else:
                            print("Variations with repetitions")
                            operation = Variations()
                            print(operation.variation_operation())
                    else:
                        self.decision = int(
                            input(
                                "\t\t\t¿¿Se repiten los elementos? \n\t\t\t(1) Si \n\t\t\t(2) No \n\t\t\topción: "
                            )
                        )
                        if self.decision == 2:
                            print("Permutations ordinary")
                            operation = Permutation()
                            print(operation.ordinary_operation())
                        else:
                            print("Permutations with repetitions")
                            operation = Permutation()
                            print(operation.variation_operation())
                else:
                    self.decision = int(
                        input(
                            "\t\t¿Se repiten los elementos? \n\t\t(1) Si \n\t\t(2) No \n\t\topción: "
                        )
                    )
                    if self.decision == 2:
                        print("Combinations ordinary")
                        operation = Combination()
                        print(operation.ordinary_operation())
                    else:
                        print("Combinations with repetitions")
                        operation = Combination()
                        print(operation.variation_operation())
            else:
                operation = PrinciplesCounting()
                print(operation.list_multiplier())


menu = Menu()
