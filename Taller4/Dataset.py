import pandas as pd
import json
import requests
import time
from pandas import json_normalize
from Taller4.SortAlgorithm import SortAlgorithm


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
    
    def available_columns(self,dataset)->str:

        return dataset.columns.values
    
    def get_Time(self,func, arr, descending=False):
        start = time.time()
        result = func(arr, descending)  
        end = time.time()
        time_Ejecution = end - start
        print(f"El tiempo de ejecución de la función fue de {time_Ejecution} segundos.")
        return result
    
    def run_quick(self, column: str, dataset, descending=False):

        array = list(dataset[column]) 

        return self.get_Time(self.quick_sort, array, descending=descending)
    
    def run_bubble(self,column,dataset,descending=False):

        array=list(dataset[column])

        return self.get_Time(self.bubble_sort,array,descending=descending)
    
    def run_counting(self,column,dataset,descending=False):

        array=list(dataset[column])

        return self.get_Time(self.counting_sort,array,descending=descending)

   
        
    


   
