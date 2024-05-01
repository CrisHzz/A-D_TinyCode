import pandas as pd
import json
import requests
import time
from pandas import json_normalize
from AlgoritmosOrdenamiento import SortAlgorithm


class Dataset(SortAlgorithm):

    def __init__(self,api:str):

        self.api=api


    def get_dataframe(self):

        url = self.api
        data = requests.get(url)
        data = json.loads(data.text)
        data = pd.json_normalize(data)

        return data
    
    def show_dataframe(dataset):

        return dataset.head(30).to_string()
    
    def available_columns(dataset)->str:

        return dataset.columns.values
    
    def get_Time(func, arr, descending=False):
        start = time.time()
        result = func(arr, descending)  
        end = time.time()
        time_Ejecution = end - start
        print(f"El tiempo de ejecución de la función fue de {time_Ejecution} segundos.")
        return result
    
    def run_quick(column: str, dataset, descending=False):

        return Dataset.get_Time(SortAlgorithm.quick_sort, dataset[column], descending=descending)

    def run_counting(column: str, dataset, descending=False):

        return Dataset.get_Time(SortAlgorithm.counting_sort, dataset[column], descending=descending)

    def run_bubble(column: str, dataset, descending=False):
        
        return Dataset.get_Time(SortAlgorithm.bubble_sort, dataset[column], descending=descending)
        
    


   
