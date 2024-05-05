from Dataset import Dataset
from colorama import init
from methodClass import methodClass
from methodMenu import methodMenu

# Se inicializa colorama para poder usar los colores en la terminal
init()

# Inicialización de las clases
Dataset = Dataset("https://www.datos.gov.co/resource/kgxf-xxbe.json")

methodClass = methodClass()

methodMenu = methodMenu()

class menu:
    def __init__(self):
        while True:
            try:
                methodMenu.menu()
                opcion = int(
                    input(
                        "\033[97;1m" + "Ingrese la opcion que desea realizar: " + "\033[0m"
                    )
                )
                print("")
    
                match opcion:
                    case 0:
                        break
                    case 1:
                        dataset = Dataset.get_dataframe()
                        print(Dataset.show_dataframe(dataset))
                    case 2:
                        dataset = Dataset.get_dataframe()
                        print("\033[93;1m" , Dataset.available_columns(dataset) , "\033[0m")
                    case 3:
                        methodClass.run_bubble_sort()
                    case 4:
                        methodClass.run_selection_sort()
                    case 5:
                        methodClass.run_insertion_sort()
                    case 6:
                        methodClass.run_merge_sort()
                    case 7:
                        methodClass.run_quick_sort()
                    case 8:
                        methodClass.run_counting_sort()
                    case 9:
                        methodClass.run_radix_sort()
                    case 10:
                        methodClass.run_heap_sort()
                    case 11:
                        methodClass.run_bucket_sort()
                if opcion < 0 or opcion > 11:
                    print(
                        "\033[91;1m"
                        + "\n\tLa opción ingresada no es válida, por favor intentelo de nuevo."
                        + "\033[0m"
                    )
            except Exception as e:
                print("\033[91;1m" + "\n\tHa ocurrido un error, por favor intentelo de nuevo." + "\033[0m")

menu = menu()