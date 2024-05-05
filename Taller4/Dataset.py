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
        print(self.quick_sort(array,descending), "\033[93;1m" + time + "\033[0m")
    
    def run_bubble_sort(self,dataset,column:str,descending:bool=False):

        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"bubble_sort")
        print(self.bubble_sort(array,descending), "\033[93;1m" + time + "\033[0m")
    
    def run_counting_sort(self,dataset,column:str,descending:bool=False):

        array = dataset[column].astype(int).tolist()
        time = self.time_Ejecution(dataset,column,"counting_sort")
        print(self.counting_sort(array,descending), "\033[93;1m" + time + "\033[0m")
    
    def run_heap_sort(self,dataset,column:str,descending:bool=False):
    
        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"heap_sort")
        print(self.heap_sort(array,descending), "\033[93;1m" + time + "\033[0m")
    
    def run_bucket_sort(self,dataset,column:str,descending:bool=False):
    
        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"bucket_sort")
        print(self.bucket_sort(array,descending), "\033[93;1m" + time + "\033[0m")
    
    def run_radix_sort(self,dataset,column:str,descending:bool=False):
        
        array = dataset[column].tolist()
        array2 = [str(num) for num in array]
        time = self.time_Ejecution(dataset,column,"radix_sort")
        print(self.radix_sort(array2,descending), "\033[93;1m" + time + "\033[0m")
    
    def run_merge_sort(self,dataset,column:str,descending:bool=False):
        
        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"merge_sort")
        print(self.merge_sort(array,descending), "\033[93;1m" + time + "\033[0m")
        
    def run_selection_sort(self,dataset,column:str,descending:bool=False):
        
        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"selection_sort")
        print(self.selection_sort(array,descending), "\033[93;1m" + time + "\033[0m")
        
    def run_insertion_sort(self,dataset,column:str,descending:bool=False):
        
        array = dataset[column].tolist()
        time = self.time_Ejecution(dataset,column,"insertion_sort")
        print(self.insertion_sort_lineal(array,descending), "\033[93;1m" + time + "\033[0m")