class SortAlgorithm:

    def __init__(self):
        pass

    def quick_sort(self,array:list, descending:bool=False)->list:
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
            
            
    def bubble_sort(self,array:list, descending:bool=False):
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


        



