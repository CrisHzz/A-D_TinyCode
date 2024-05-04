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

    def heapify(array, i, descending=False):
        # Verificamos si el nodo tiene 2 hijos
        if 2 * i + 2 <= len(array) - 1:
            if descending:
                if array[2 * i + 1] >= array[2 * i + 2]:  # Buscamos el mayor de los hijos
                    child = 2 * i + 1
                else:
                    child = 2 * i + 2
            else:
                if array[2 * i + 1] <= array[2 * i + 2]:  # Buscamos el menor de los hijos
                    child = 2 * i + 1
                else:
                    child = 2 * i + 2

            if descending:
                if array[i] < array[child]:  # Comparamos el valor del padre con el hijo mayor
                    aux = array[i]
                    array[i] = array[child]
                    array[child] = aux

                    heapify(array, child, descending)  # Cambiamos el nodo con el que acabamos de intercambiar que ahora es el máximo
            else:
                if array[i] > array[child]:  # Comparamos el valor del padre con el hijo menor
                    aux = array[i]
                    array[i] = array[child]
                    array[child] = aux

                    heapify(array, child, descending)  # Cambiamos el nodo con el que acabamos de intercambiar que ahora es el mínimo

        # Si solo se tiene un hijo
        elif 2 * i + 1 <= len(array) - 1:
            if descending:
                if array[i] < array[2 * i + 1]:  # Volvemos a mirar si el padre es menor que el hijo e intercambiarlos
                    aux = array[i]
                    array[i] = array[2 * i + 1]
                    array[2 * i + 1] = aux
            else:
                if array[i] > array[2 * i + 1]:  # Volvemos a mirar si el padre es mayor que el hijo e intercambiarlos
                    aux = array[i]
                    array[i] = array[2 * i + 1]
                    array[2 * i + 1] = aux

        return array

    def heapsort(array:list, descending=False):
        try:
            if not isinstance(array, list):
                raise TypeError("El parámetro 'array' debe ser una lista.")

            if not isinstance(descending, bool):
                raise TypeError("El parámetro 'descending' debe ser un valor booleano.")

            l = []  # inicializar una lista final
            for i in range(len(array)//2 - 1, -1, -1):
                array = heapify(array, i, descending)

            for i in range(0, len(array)):
                aux = array[0]
                array[0] = array[len(array)-1]
                array[len(array) - 1] = aux

                l.append(aux)

                array = array[:len(array)-1]
                array = heapify(array, 0, descending)

            return l

        except (TypeError, ValueError) as e:
            print("Ingrese una lista válida")  # Imprimimos el mensaje de error
        
    def radixsort(array:list, descending=False):  # los números que recibe deben ser tipo cadena y no tipo número
        try:
            if not isinstance(array, list):
                raise TypeError("El parámetro 'array' debe ser una lista.")

            if not isinstance(descending, bool):
                raise TypeError("El parámetro 'descending' debe ser un valor booleano.")

            if not all(isinstance(element, str) for element in array):
                raise ValueError("Los elementos del 'array' deben ser cadenas de texto.")

            n = 0
            for e in array:
                if len(e) > n:
                    n = len(e)

            for i in range(0, len(array)):
                while len(array[i]) < n:
                    array[i] = "0" + array[i]

            for j in range(n - 1, -1, -1):
                groups = [[] for i in range(10)]

                for i in range(len(array)):
                    groups[int(array[i][j])].append(array[i])

                if descending:
                    array = [x for group in reversed(groups) for x in group]
                else:
                    array = [x for group in groups for x in group]

            return [int(i) for i in array]

        except (TypeError, ValueError) as e:
            print("Ingrese una lista válida de cadenas de texto")  # Imprimimos el mensaje de error

prueba=SortAlgorithm()

