from Dataset import Dataset
from colorama import init

# Se inicializa colorama para poder usar los colores en la terminal
init()

Dataset = Dataset("https://www.datos.gov.co/resource/kgxf-xxbe.json")

class methodClass:
    
    def run_bubble_sort(self):
        print("\033[92;1m" + "Bubble Sort\n" + "\033[0m")
        while True:
            
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                 "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
                                  
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
                            
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_bubble_sort(dataset, column, descending)
            break
    
    def run_selection_sort(self):
        print("\033[92;1m" + "Selection Sort\n" + "\033[0m")
        while True:
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                + "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
                
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
            
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_selection_sort(dataset, column, descending)
            break
        
    def run_insertion_sort(self):
        print("\033[92;1m" + "Insertion Sort\n" + "\033[0m")
        while True:
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                + "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_insertion_sort(dataset, column, descending)
            break
        
    def run_merge_sort(self):
        print("\033[92;1m" + "Merge Sort\n" + "\033[0m")
        while True:
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                + "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_merge_sort(dataset, column, descending)
            break
    
    def run_quick_sort(self):
        print("\033[92;1m" + "Quick Sort\n" + "\033[0m")
        while True:
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                + "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_quick_sort(dataset, column, descending)
            break
    
    def run_counting_sort(self):
        print("\033[92;1m" + "Counting Sort\n" + "\033[0m")
        while True:
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                + "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_counting_sort(dataset, column, descending)
            break
        
    def run_radix_sort(self):
        print("\033[92;1m" + "Radix Sort\n" + "\033[0m")
        while True:
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                + "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_radix_sort(dataset, column, descending)
            break
    
    def run_heap_sort(self):
        print("\033[92;1m" + "Heap Sort\n" + "\033[0m")
        while True:
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                + "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_heap_sort(dataset, column, descending)
            break
    
    def run_bucket_sort(self):
        print("\033[92;1m" + "Bucket Sort\n" + "\033[0m")
        while True:
            dataset = Dataset.get_dataframe()
            column = input(
                "\033[94;1m"
                + "\tIngrese la columna que desea ordenar: "
                + "\033[0m"
            )
            descending = input(
                "\033[94;1m"
                + "\t¿Desea ordenar de forma descendente? (True/False): "
                + "\033[0m"
            ).capitalize()
            for i in Dataset.available_columns(dataset):
                if column not in Dataset.available_columns(dataset):
                    print(
                        "\033[91;1m"
                        + "\n\tLa columna ingresada no existe en el dataset."
                        + "\033[0m"
                    )
                    break
            if descending != "True" and descending != "False":
                print(
                    "\033[91;1m"
                    + "\n\tSolo puedes ingresar True o False."
                    + "\033[0m"
                )
                break
            descending = (
                "True" if (descending == "Si") else descending == "False"
            )
            print("")
            Dataset.run_bucket_sort(dataset, column, descending)
            break