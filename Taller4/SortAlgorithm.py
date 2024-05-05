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
            while True:
                # Si hay una cadena en el array, lanza una excepción
                if any(isinstance(i, str) for i in array):
                    raise ValueError("El array contiene una cadena de texto")
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if descending:
                            if array[j] < array[j + 1] :
                                array[j], array[j + 1] = array[j + 1], array[j]
                        else:
                            if array[j] > array[j + 1] :
                                array[j], array[j + 1] = array[j + 1], array[j]
                # Si el array está ordenado, rompe el ciclo
                if array == sorted(array, reverse=descending):
                    break
            return array

    
    # Metodo para ordenar por el metodo de Quick Sort
    def quick_sort(self, array:list, descending:bool=False):
        if len(array) == 0:
            return []
        elif len(array) == 1:
            return array
        else:
            if any(isinstance(i, int) for i in array):
                raise ValueError("El array contiene un entero")
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
            if any(isinstance(i, float) or isinstance(i, str) or i < 0 for i in array):
                raise ValueError("El array contiene un decimal, un negativo o una cadena")
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
        # Si hay una cadena en el array, lanza una excepción
        if any(isinstance(i, str) for i in array):
            raise ValueError("El array contiene una cadena")
        else:
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
        # Función para ordenar un cubo utilizando el algoritmo de inserción
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            # Movemos los elementos mayores hacia la derecha para hacer espacio para el elemento actual
            while j >= 0 and key < bucket[j]:
                bucket[j + 1] = bucket[j]
                j -= 1
            # Insertamos el elemento actual en su posición correcta
            bucket[j + 1] = key
        return bucket


    def bucket_sort(self, array:list, descending=False):
        if len(array) == 0:
            return array
        elif any(isinstance(i, int) or isinstance(i, str) or (isinstance(i, float) and (i < 0 or i > 1)) for i in array):
            raise ValueError("El array contiene un entero, un decimal fuera del rango de 0 a 1 o una cadena")
        else:

            # Encontramos el valor mínimo y máximo del array
            min_val = min(array)
            max_val = max(array)

            # Calculamos el rango de cada cubo
            bucket_range = max((max_val - min_val) / len(array), 1)

            # Creamos una lista de cubos vacíos
            bucket_list = [[] for _ in range(len(array))]

            # Distribuimos los elementos del array en los cubos correspondientes
            for i in range(len(array)):
                # Aseguramos que el valor calculado de bucket_index esté dentro de los límites válidos de bucket_list
                bucket_index = min(int((array[i] - min_val) / bucket_range), len(bucket_list) - 1)
                bucket_list[bucket_index].append(array[i])

            # Ordenamos cada cubo utilizando el algoritmo de inserción
            sorted_array = []
            for bucket in bucket_list:
                if len(bucket) > 0:
                    sorted_bucket = self.insertion_sort(bucket)
                    sorted_array.extend(sorted_bucket)

            # Devolvemos el array ordenado, en orden ascendente o descendente según el parámetro 'descending'
            if descending:
                return sorted_array[::-1]
            else:
                return sorted_array
        
        
    # Metodo para ordenar por el metodo de Radix Sort
    def radixsort(self, array:list, descending=False):
        # Si hay una cadena, un decimal o un negativo en el array, lanza una excepción
        if any(isinstance(i, str) or isinstance(i, float) or (isinstance(i, int) and i < 0) for i in array):
            raise ValueError("El array contiene una cadena, un decimal o un entero negativo")
        else:
            n = 0 # n tomara el valor del max de digitos que encuentre entre los numeros de la lista
            for e in array: #se recorre cada elemento dee la lista para hallar ese valor
                if len(e) > n:
                    n = len(e)

            # ponerle el numero de 0 a la izquierda a los numeros que les haga falta pa q todos tengan el mismo num de digitos
            for i in range(0, len(array)):
                while len(array[i]) < n: #nos aseguramos que todos esten igual
                    array[i] = "0" + array[i] #concatenamos

            #iteramos sobre cada digito de los numeros
            for j in range(n - 1, -1, -1):
                groups = [[] for i in range(10)] #creamos los grupos de acuerdo al digito que se este evaluando

                for i in range(len(array)):
                    groups[int(array[i][j])].append(array[i])

                if descending:
                    array = [x for group in reversed(groups) for x in group]
                else:
                    array = [x for group in groups for x in group]

            return [int(i) for i in array]
        

    
    def merge(self, left:list, right:list, descending:bool=False):
        result = []
        while left and right:
            if descending:
                if left[0] > right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            else:
                if left[0] < right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
        result.extend(left if left else right)
        return result

    def merge_sort(self, array:list, descending:bool=False):
    
        if any(isinstance(i, str) for i in array):
            raise ValueError("El array contiene una cadena")
        else:
            if len(array) <= 1:
                return array
            mid = len(array) // 2
            left = self.merge_sort(array[:mid], descending)
            right = self.merge_sort(array[mid:], descending)
            return self.merge(left, right, descending)
        

    def selection_sort(self, array:list, descending:bool=False):
        if len(array) == 0:
            return []
        elif len(array) == 1:
            return array
        else:
            n = len(array)
            for i in range(n):
                if any(isinstance(i, str) for i in array):
                    raise ValueError("El array contiene una cadena")
                min_index = i
                for j in range(i + 1, n):
                    if descending:
                        if array[j] > array[min_index]:
                            min_index = j
                    else:
                        if array[j] < array[min_index]:
                            min_index = j
                array[i], array[min_index] = array[min_index], array[i]
            return array    
    

    def insertion_sort_lineal(self,array, descending:bool=False):

        if any(isinstance(x, str) for x in array):
            raise ValueError("El array contiene una cadena")
        else:
            for i in range(1, len(array)):
                key = array[i]
                j = i - 1
                if descending:
                    while j >= 0 and key > array[j]:
                        array[j + 1] = array[j]
                        j -= 1
                else:
                    while j >= 0 and key < array[j]:
                        array[j + 1] = array[j]
                        j -= 1
                array[j + 1] = key
            return array
        

