class SortAlgorithm:

    def __init__(self):
        pass

    def quick_sort(array:list, descending:bool=False)->list:
        while True:
            try:
                if not isinstance(array, list):
                    raise TypeError("El parámetro 'array' debe ser una lista.")

                if not isinstance(descending, bool):
                    raise TypeError("El parámetro 'descending' debe ser un valor booleano.")

                if len(array) <= 1:
                    return array
                else:
                    pivot = array.pop()

                greater = []
                lower = []

                for element in array:
                    if element > pivot:
                        greater.append(element)
                    else:
                        lower.append(element)

                    if descending:
                        return SortAlgorithm.quick_sort(greater, descending) + [pivot] + SortAlgorithm.quick_sort(lower, descending)
                    else:
                        return SortAlgorithm.quick_sort(lower, descending) + [pivot] + SortAlgorithm.quick_sort(greater, descending)
            
                break  # Si no se lanzan excepciones, salimos del bucle while
            except (TypeError, ValueError) as e:
                    print("ingrese los parametros correctos")  # Imprimimos el mensaje de error
                    break

    def bubble_sort(array:list, descending:bool=False)->list:
        try:
            if not isinstance(array, list):
                raise TypeError("El parámetro 'array' debe ser una lista.")

            if not isinstance(descending, bool):
                raise TypeError("El parámetro 'descending' debe ser un valor booleano.")

            n = len(array)

            for i in range(n):
                for j in range(0, n - i - 1):
                    if descending:
                        if array[j] < array[j + 1]:
                            array[j], array[j + 1] = array[j + 1], array[j]
                    else:
                        if array[j] > array[j + 1]:
                            array[j], array[j + 1] = array[j + 1], array[j]
            return array

        except (TypeError, ValueError) as e:
            print("Ingrese una lista válida de números")  # Imprimimos el mensaje de error
    
    def counting_sort(array:list, descending:bool=False)->list:
        try:
            if not isinstance(array, list):
                raise TypeError("El parámetro 'array' debe ser una lista.")

            if not isinstance(descending, bool):
                raise TypeError("El parámetro 'descending' debe ser un valor booleano.")

            if not all(isinstance(element, (int)) for element in array):
                raise ValueError("Los elementos del 'array' deben ser números enteros")

            max_val = max(array)
            count = [0] * (max_val + 1)

            for num in array:
                count[num] += 1

            i = 0
            if descending:
                for num in range(max_val, -1, -1):
                    while count[num] > 0:
                        array[i] = num
                        i += 1
                        count[num] -= 1
            else:
                for num in range(len(count)):
                    while count[num] > 0:
                        array[i] = num
                        i += 1
                        count[num] -= 1

            return array

        except (TypeError, ValueError) as e:
            print("Ingrese una lista válida de números enteros")  # Imprimimos el mensaje de error


prueba=SortAlgorithm()

