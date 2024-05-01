class SortAlgorithm:

    def __init__(self):
        pass

    def quick_sort(array:list, descending:bool=False)->list:
            
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


    def bubble_sort(array:list, descending:bool=False):

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

    
    def counting_sort(array:list, descending:bool=False):
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



