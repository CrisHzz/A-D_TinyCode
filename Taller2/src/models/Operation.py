from abc import ABC, abstractmethod

import math

class Operation(ABC):

    def __init__(self,n:int,r:int,variables:list):
        self.n=n
        self.r=r
        self.variables=variables

    def classicFactorial(self,n:int)->int:

        return math.factorial(n)
    

    @abstractmethod
    def ordinary_operation(self):
        
        pass
    
    @abstractmethod
    def variation_operation(self):

        pass

    def find_variables(self,):
        pass

    






