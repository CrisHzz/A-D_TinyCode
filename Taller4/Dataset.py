import pandas as pd
import json
import requests
import time
from pandas import json_normalize
from SortAlgorithm import SortAlgorithm


class Dataset(SortAlgorithm):

    def __init__(self,api:str):

        self.api=api


    def get_dataframe(self):

        url = self.api
        data = requests.get(url)
        data = json.loads(data.text)
        data = pd.json_normalize(data)

        return data
    
    def show_dataframe(self,dataset):

        return dataset.head(30).to_string()
    
    def available_columns(self,dataset):

        return dataset.columns.values
    
    def time_Ejecution(self,dataset,column:str,algorithm:str):

        array = dataset[column].tolist()
        start = time.time()
        if algorithm == "quick_sort":
            self.quick_sort(array)
        elif algorithm == "bubble_sort":
            self.bubble_sort(array)
        elif algorithm == "counting_sort":
            self.counting_sort(array)
        end = time.time()

        return f"El tiempo de ejecucion fue de {end-start} segundos"


    def run_quick_sort(self,dataset,column:str,descending:bool=False):

        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"quick_sort")
        return self.quick_sort(array,descending), time
    
    def run_bubble_sort(self,dataset,column:str,descending:bool=False):

        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"bubble_sort")
        return self.bubble_sort(array,descending), time
    
    def run_counting_sort(self,dataset,column:str,descending:bool=False):

        array = dataset[column].astype(int).tolist()
        time = self.time_Ejecution(dataset,column,"counting_sort")
        return self.counting_sort(array,descending), time
    
    def run_heap_sort(self,dataset,column:str,descending:bool=False):
    
        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"heap_sort")
        return self.heapsort(array,descending), time
    
    def run_bucket_sort(self,dataset,column:str,descending:bool=False):
    
        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"bucket_sort")
        return self.bucket_sort(array,descending), time
    
    def run_radix_sort(self,dataset,column:str,descending:bool=False):
        
        array = dataset[column].tolist()
        array2 = [str(num) for num in array]
        time = self.time_Ejecution(dataset,column,"radix_sort")
        return self.radixsort(array2,descending), time
