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
    l = [] #inicializar una lista final
    for i in range(len(array)//2 - 1, -1, -1): #recorro el rango desde el valor de la lista (parte entera) y como queremos llegar al 0 hay que ir decrementando
        array = heapify(array, i, descending) #aqui se ira modificando el ordeen de los nodos del arbol que representamos como lista

    for i in range(0, len(array)):
        aux = array[0] #guardamos el primer elemento
        array[0] = array[len(array)-1] #pasamos el ultimo a la primera posicion
        array[len(array) - 1] = aux #lo que teniamos en primer lugar lo pasamos al final de la lista

        l.append(aux) #vvamos agregando el elemento menor en la lista final

        array = array[:len(array)-1] #eliminamos el ultimo elemento de la lista cortando el ultimo elemento
        array = heapify(array, 0, descending) #modificamos el orden de los nodos va a iniciar deesdee el nodo 0

    return l


#ejemplo de uso:
#lista = [4, 8, 19, 177, 2, 10, 6, 178]
#print(lista)
#print(heapsort(lista, True)) # aqui solo se pasa si es falso o verdadero para el orden de la lista


