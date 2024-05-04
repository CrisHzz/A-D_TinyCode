def radixsort(array:list, descending=False): #los numeeros que reciben deben de ser tipo cadena y no tipo numero
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

#ejemplo de uso:
#l = [4, 8, 19, 177, 2, 10, 6, 178]
#l2 = [str(num) for num in l]  #se pasa la lista a tipo cadena usando str
#print(l)
#print(radixsort(l2, False))  # aqui solo se pasa si es falso o verdadero para el orden de la lista
