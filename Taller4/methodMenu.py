
class methodMenu:
    def __init__(self) -> None:
        self.lineas1 = (
                "\033[97;1m"
                + "/----------------------------------------------------------------------------------\ "
                + "\033[0m"
            )
        self.lineas2 = (
                "\033[97;1m"
                + "\----------------------------------------------------------------------------------/"
                + "\033[0m"
            )
        self.lineas3 = (
                "\033[97;1m"
                + "|----------------------------------------------------------------------------------|"
                + "\033[0m"
            )
    
    def menu(self):
        print("\n" + self.lineas1)
        print(
            "\033[97;1m"
            + "| El usario debe de hacer Ctrl + Menos (-), para poder visualizar bien el Dataset  |"
            + "\033[0m"
        )
        print(self.lineas2 + "\n")
        print(self.lineas1)
        print(
            "\033[97;1m"
            + " | Bienvenido al menú de los métodos de ordenamiento                              |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 1. Mostrar Dataframe con 30 filas                                              |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 2. Mostrar Columnas                                                            |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 3. Ordenar por Bubble Sort                                                     |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 4. Ordenar por Selection Sort                                                  |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 5. Ordenar por Insetion Sort                                                   |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 6. Ordenar por Merge Sort                                                      |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 7. Ordenar por Quick Sort                                                      |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 8. Ordenar por Counting Sort                                                   |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 9. Ordenar por Radix Sort                                                      |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 10. Ordenar por Heap Sort                                                      |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 11. Ordenar por Bucket Sort                                                    |"
            + "\033[0m"
        )
        print(self.lineas3)
        print(
            "\033[97;1m"
            + " | 0. Salir                                                                       |"
            + "\033[0m"
        )
        print(self.lineas2 + "\n")