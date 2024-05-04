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
    
    def available_columns(self,dataset)->str:

        return dataset.columns.values
    
    def time_Ejecution(self,dataset,column:str,algorithm:str)->str:

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


    def run_quick_sort(self,dataset,column:str,descending:bool=False)->list:

        array = dataset[column].tolist()

        return self.quick_sort(array,descending)
    
    def run_bubble_sort(self,dataset,column:str,descending:bool=False)->list:

        array = dataset[column].tolist()

        return self.bubble_sort(array,descending)
    
    def run_counting_sort(self,dataset,column:str,descending:bool=False)->list:

        array = dataset[column].astype(int).tolist()

        return self.counting_sort(array,descending)
   

prueba=Dataset("https://www.datos.gov.co/resource/kgxf-xxbe.json")

data=prueba.get_dataframe()


quick=prueba.run_counting_sort(data,"periodo",False)

print(quick)


        
    


   
