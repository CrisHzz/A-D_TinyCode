class SortAlgorithm:

    def __init__(self):
        pass
    
    
    # Metodo para ordenar por el metodo de Bubble Sort
    def bubble_sort(self, array:list, descending:bool=False):
        if len(array) == 0:
            return []
        elif len(array) == 1:
            return array
        else:
            n = len(array)

            for i in range(n):
                for j in range(0, n - i - 1):
                    if descending:
                        if array[j] < array[j + 1] :
                            array[j], array[j + 1] = array[j + 1], array[j]
                    else:
                        if array[j] > array[j + 1] :
                            array[j], array[j + 1] = array[j + 1], array[j]
            return array
    
    
    # Metodo para ordenar por el metodo de Quick Sort
    def quick_sort(self,array:list, descending:bool=False):
        if len(array) == 0:
            return []
        elif len(array) == 1:
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
            return self.quick_sort(greater, descending) + [pivot] + self.quick_sort(lower, descending)
        else:
            return self.quick_sort(lower, descending) + [pivot] + self.quick_sort(greater, descending)


    # Metodo para ordenar por el metodo de Counting Sort
    def counting_sort(self, array:list, descending:bool=False):

        if len(array) == 0:
            return []
        elif len(array) == 1:
            return array
        else:
            max_value = max(array)
            min_value = min(array)
            counting_array = [0] * (max_value - min_value + 1)
            for number in array:
                counting_array[number - min_value] += 1
            index = 0
            for i in range(len(counting_array)):
                while counting_array[i] > 0:
                    array[index] = i + min_value
                    index += 1
                    counting_array[i] -= 1
            if descending:
                return array[::-1]
            else:
                return array
    
    
    # Metodo para ordenar por el metodo de Heap Sort        
    def heapify(self, array:list, i, descending:bool=False):
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

                    return self.heapify(array, child, descending)  # Cambiamos el nodo con el que acabamos de intercambiar que ahora es el máximo
            else:
                if array[i] > array[child]:  # Comparamos el valor del padre con el hijo menor
                    aux = array[i]
                    array[i] = array[child]
                    array[child] = aux

                    return self.heapify(array, child, descending)  # Cambiamos el nodo con el que acabamos de intercambiar que ahora es el mínimo

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
    
    def heap_sort(self, array:list, descending:bool=False):
        l = [] #inicializar una lista final
        for i in range(len(array)//2 - 1, -1, -1): #recorro el rango desde el valor de la lista (parte entera) y como queremos llegar al 0 hay que ir decrementando
            array = self.heapify(array, i, descending) #aqui se ira modificando el ordeen de los nodos del arbol que representamos como lista

        for i in range(0, len(array)):
            aux = array[0] #guardamos el primer elemento
            array[0] = array[len(array)-1] #pasamos el ultimo a la primera posicion
            array[len(array) - 1] = aux #lo que teniamos en primer lugar lo pasamos al final de la lista

            l.append(aux) #vvamos agregando el elemento menor en la lista final

            array = array[:len(array)-1] #eliminamos el ultimo elemento de la lista cortando el ultimo elemento
            array = self.heapify(array, 0, descending) #modificamos el orden de los nodos va a iniciar deesdee el nodo 0

        return l    
    
    
    # Metodo para ordenar por el metodo de Bucket Sort
    def insertion_sort(self, bucket):
        try:
            for i in range(1, len(bucket)):
                key = bucket[i]
                j = i - 1
                while j >= 0 and key < bucket[j]:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                bucket[j + 1] = key
            return bucket

        except Exception as e:
            print("Se produjo un error al ordenar el cubo:", e)


    def bucket_sort(self, array:list, descending=False):
        try:
            if not isinstance(array, list):
                raise TypeError("El parámetro 'array' debe ser una lista.")

            if not isinstance(descending, bool):
                raise TypeError("El parámetro 'descending' debe ser un valor booleano.")

            if len(array) == 0:
                return array

            min_val = min(array)
            max_val = max(array)

            bucket_range = max((max_val - min_val) / len(array), 1)

            bucket_list = [[] for _ in range(len(array))]

            for i in range(len(array)):
                bucket_index = min(int((array[i] - min_val) / bucket_range), len(bucket_list) - 1)
                bucket_list[bucket_index].append(array[i])

            sorted_array = []
            for bucket in bucket_list:
                if len(bucket) > 0:
                    sorted_bucket = self.insertion_sort(bucket)
                    sorted_array.extend(sorted_bucket)

            if descending:
                return sorted_array[::-1]
            else:
                return sorted_array

        except (TypeError, ValueError) as e:
            print("Se produjo un error al ordenar el array:", e)
        
        
    # Metodo para ordenar por el metodo de Radix Sort
    def radixsort(self, array:list, descending=False):
        try:
            if not isinstance(array, list):
                raise TypeError("El parámetro 'array' debe ser una lista.")

            if not isinstance(descending, bool):
                raise TypeError("El parámetro 'descending' debe ser un valor booleano.")

            for e in array:
                if not isinstance(e, str) or not e.isdigit() or int(e) < 0:
                    raise ValueError("Los elementos del 'array' deben ser cadenas de texto que representen enteros positivos.")

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
            print("Se produjo un error al ordenar la lista:", e)
