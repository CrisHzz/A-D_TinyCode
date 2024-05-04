from Dataset import Dataset
from colorama import init

# Se inicializa colorama para poder usar los colores en la terminal
init()

Dataset = Dataset("https://www.datos.gov.co/resource/kgxf-xxbe.json")

class menu:
    def __init__(self):
        
        while True:
            lineas1 = "/--------------------------------------------------------------------------------\ " 
            lineas2 = "\--------------------------------------------------------------------------------/" 
            lineas3 = "|--------------------------------------------------------------------------------|"
            try:
                print("\n" + lineas1)
                print("|El usario debe de hacer Ctrl + Menos (-), para poder visualizar bien el Dataset |")
                print(lineas2 + "\n")
                print(lineas1)
                print("|Bienvenido al menú de los métodos de ordenamiento                               |")
                print(lineas3)
                print("|1. Mostrar Dataframe con 30 filas                                               |")
                print(lineas3)
                print("|2. Mostrar Columnas                                                             |")
                print(lineas3)
                print("|3. Ordenar por Bubble Sort                                                      |")
                print(lineas3)
                print("|4. Ordenar por Selection Sort                                                   |")
                print(lineas3)
                print("|5. Ordenar por Insetion Sort                                                    |")
                print(lineas3)
                print("|6. Ordenar por Merge Sort                                                       |")
                print(lineas3)
                print("|7. Ordenar por Quick Sort                                                       |")
                print(lineas3)
                print("|8. Ordenar por Counting Sort                                                    |")
                print(lineas3)
                print("|9. Ordenar por Radix Sort                                                      |")
                print(lineas3)
                print("|10. Ordenar por Heap Sort                                                       |")
                print(lineas3)
                print("|11. Ordenar por Bucket Sort                                                     |")
                print(lineas3)
                print("|0. Salir                                                                        |")
                print(lineas2 + "\n")

                opcion = int(input("Ingrese la opcion que desea realizar: "))
                print("")
                
                match opcion:
                    case 0:
                        break
                    case 1:
                        dataset = Dataset.get_dataframe()
                        print(Dataset.show_dataframe(dataset))
                    case 2:
                        dataset = Dataset.get_dataframe()
                        print(Dataset.available_columns(dataset))
                    case 3:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_bubble_sort(dataset, column, descending))
                    case 4:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_selection_sort(dataset, column, descending))
                    case 5:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_insertion_sort(dataset, column, descending))
                    case 6:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_merge_sort(dataset, column, descending))
                    case 7:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_quick_sort(dataset, column, descending))
                    case 8:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_counting_sort(dataset, column, descending))
                    case 9:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_radix_sort(dataset, column, descending))
                    case 10:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_heap_sort(dataset, column, descending))
                    case 11:
                        dataset = Dataset.get_dataframe()
                        column = input("Ingrese la columna que desea ordenar: ")
                        descending = input("¿Desea ordenar de forma descendente? (True/False): ")
                        print(Dataset.run_bucket_sort(dataset, column, descending))
            except Exception as e:
                print(e)
                print("Ha ocurrido un error, por favor intentelo de nuevo.")
    

menu = menu()