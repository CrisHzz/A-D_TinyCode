class SortAlgorithm:

    def __init__(self):
        pass

    def quick_sort(array:list)->list:
        base = len(array)
        if base <= 1:
            return array
        
        pivote = array.pop()
        array1 = []
        array2 = []

        for i in array:
            if i <= pivote:
                array1.append(i)
            else:
                array2.append(i)

        array1 = SortAlgorithm.quickSort(array1)
        array2 = SortAlgorithm.quickSort(array2)

        return array1 + [pivote] + array2
    
    def bubble_sort(array:list):

        n = len(array)

        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1] :
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array
    
    def counting_sort(lista):
        max_val = max(lista)
        count = [0] * (max_val + 1)

        for num in lista:
            count[num] += 1

        i = 0
        for num in range(len(count)):
            while count[num] > 0:
                lista[i] = num
                i += 1
                count[num] -= 1
        return lista




