from abc import ABC, abstractmethod

import math

class Operation(ABC):

    def __init__(self,n:int,r:int,variables:list):
        self.n=n
        self.r=r
        self.variables=variables

    def classicFactorial(self):
        return factorial





