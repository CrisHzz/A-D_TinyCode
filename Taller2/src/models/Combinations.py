from Operation import Operation

class Combinations(Operation):
    
     def __init__(self):
        super().__init__(2,4,[])
        repeat = int(input("Seleccione 1 si los datos que se van a agrupar se repiten o 2 si no se repiten: "))
        if repeat == 1: 
            self.ordinary_operation()
        else: 
            self.variation_operation()

     def ordinary_operation(self):#se repiten 
        self.n=int(input("En cuantos numeros desea agrupar los datos"))
        self.r=int(input("Escriba el numero de datos en total que se tiene"))
        num = (self.r) + (self.n-1)
        deno2 = self.r - 1
        num_fac1= self.classicFactorial(num)
        deno_fac1=self.classicFactorial(self.n) * self.classicFactorial(deno2)
        result = num_fac1 / deno_fac1
        return  result

     def variation_operation(self):#no se repiten 
        self.n=int(input("En cuantos numeros desea agrupar los datos"))
        self.r=int(input("Escriba el numero de datos en total que se tiene"))
        num_fac1= self.classicFactorial(self.r)
        deno_fac1=self.classicFactorial(self.n) * self.classicFactorial(self.r - self.n)
        result = num_fac1 / deno_fac1
        return  result

c=Combinations()