def heapify(array, i):
    #verificamos si el nodo tiene 2 hijos
    if 2 * i + 2 <= len(array) - 1:
        if array[2 * i + 1] <= array[2 * i + 2]: #buscamos el menor de los hijos si iz o dere
            min = 2 * i + 1
        else:
            min = 2 * i + 2

        if array[i] > array[min]: #comparamos el valor del padre es mayor que al hijo menor, si es asi realizamos el intercambio
            aux = array[i]
            array[i] = array[min]
            array[min] = aux

            heapify(array, min) #cambiamos el nodo con el q acabamos de intercambiar que ahora es el minimo

    #si solo se tiene un hijo
    elif 2 * i + 1 <= len(array) - 1:
        if array[i] > array[2 * i + 1]: #volvemos a mirar si el padre es mayor que el hijo e intercambiarlos
            aux = array[i]
            array[i] = array[2 * i + 1]
            array[2 * i + 1] = aux

    return array


def heapsort(array:list):
    l = [] #inicializar una lista final
    for i in range(len(array)//2 - 1, -1, -1): #recorro el rango desde el valor de la lista (parte entera) y como queremos llegar al 0 hay que ir decrementando
        array = heapify(array, i) #aqui se ira modificando el ordeen de los nodos del arbol que representamos como lista

    for i in range(0, len(array)):
        aux = array[0] #guardamos el primer elemento
        array[0] = array[len(array)-1] #pasamos el ultimo a la primera posicion
        array[len(array) - 1] = aux #lo que teniamos en primer lugar lo pasamos al final de la lista

        l.append(aux) #vvamos agregando el elemento menor en la lista final

        array = array[:len(array)-1] #eliminamos el ultimo elemento de la lista cortando el ultimo elemento
        array = heapify(array, 0) #modificamos el orden de los nodos va a iniciar deesdee el nodo 0

    return l


#ejemplo de uso:
#lista = [4, 8, 19, 177, 2, 10, 6, 178]
#print(lista)
#print(heapsort(lista))


