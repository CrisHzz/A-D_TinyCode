from abc import ABC, abstractmethod

import math

class Operation(ABC):

    def __init__(self,n:int,r:int,variables:list):
        self.n=n
        self.r=r
        self.variables=variables

    def classicFactorial(self):
        if not isinstance(self.n, int):
            raise ValueError("Tiene que ser entero")
        
        if self.n < 0:
            raise ValueError("Positivo porfavor!")
        return math.factorial(self.n)
    
    def find_variables(self):
        while True:
            try:
                num_variables = int(input("Porfavor ingrese el numero de variables: "))
                self.variables = []

                for i in range(num_variables):
                    while True:
                        try:
                            variable = int(input(f"Ingrese la variable N°{i+1}: "))
                            self.variables.append(variable)
                            break 
                        except ValueError:
                            print("Error: Tienes que digitar un natural para la variable.")
                            continue  

                break
            except ValueError:
                print("Numero incorrecto, sigue intentado")


    @abstractmethod
    def ordinary_operation(self):
        
        pass
    
    @abstractmethod
    def variation_operation(self):

        pass



