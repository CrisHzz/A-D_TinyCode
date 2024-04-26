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
    
    def get_Time(func, arr):

        inicio = time.time()
        resultado = func(arr)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"El tiempo de ejecución de la función fue de {tiempo_ejecucion} segundos.")

        return resultado
    
    def run_quick(columna:str,dataset):

        return Dataset.medir_tiempo(SortAlgorithm.quick_sort,dataset[columna])
    
    def run_counting(columna:str,dataset):

        return Dataset.medir_tiempo(SortAlgorithm.counting_sort,dataset[columna])
    
    def run_bubble(columna:str,dataset):

        return Dataset.medir_tiempo(SortAlgorithm.bubble_sort,dataset[columna])
     
    


   
