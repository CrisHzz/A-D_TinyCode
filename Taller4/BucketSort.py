def insertion_sort(bucket):
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


def bucket_sort(array: list, descending=False):
    if len(array) == 0:
        return array

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
            sorted_bucket = insertion_sort(bucket)
            sorted_array.extend(sorted_bucket)

    # Devolvemos el array ordenado, en orden ascendente o descendente según el parámetro 'descending'
    if descending:
        return sorted_array[::-1]
    else:
        return sorted_array


# Ejemplo de uso:
#l = [4, 8, 19, 177, 2, 10, 6, 178, 87, 23, 991, 4]
#print(l)
#print(bucket_sort(l, False))
