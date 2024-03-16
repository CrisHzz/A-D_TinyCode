from abc import ABC, abstractmethod

import math

class Operation(ABC):

    def __init__(self,n:int,r:int,variables:list):
        self.n=n
        self.r=r
        self.variables=variables

    def classicFactorial(self,n:int)->int:

        return math.factorial(n)
    
    def find_variables(self):
        while True:
            try:
                num_variables = int(input("Please enter the number of the variables: "))
                self.variables = []

                for i in range(num_variables):
                    while True:
                        try:
                            variable = int(input(f"Please enter the variable N°{i+1}: "))
                            self.variables.append(variable)
                            break 
                        except ValueError:
                            print("Error: You must enter an integer value for the variable.")
                            continue  

                print(f"The variables entered are: {self.variables}")
                break
            except ValueError:
                print("Incorrect number, please try again.")



            
            
    

    @abstractmethod
    def ordinary_operation(self):
        
        pass
    
    @abstractmethod
    def variation_operation(self):

        pass



