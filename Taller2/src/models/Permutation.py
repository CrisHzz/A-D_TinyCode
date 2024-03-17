from Operation import Operation

class Permutation(Operation):

    def circular_permutation(self):
        if not isinstance(self.n, int):
            raise ValueError("Tiene que ser un entero")
        if self.n < 0:
            raise ValueError("Tiene que ser un positivo")
        return self.classicFactorial(self.n) - 1

    def ordinary_operation(self):
        if not isinstance(self.n, int) or not isinstance(self.r, int):
            raise ValueError("Tiene que ser un entero")
        if self.n < 0 or self.r < 0:
            raise ValueError("Tiene que ser un positivo")
        
        return self.classicFactorial(self.n) / self.classicFactorial(self.n - self.r)


    def variation_operation(self):
        if not isinstance(self.n, int) or not isinstance(self.r, int):
            raise ValueError("Tiene que ser un entero")
    
        if self.n < 0:
            raise ValueError("Tiene que ser un positivo")
        
        numerator = self.classicFactorial(self.n)

        denominator = 1

        for variable in self.variables:

            denominator *= self.classicFactorial(variable)

        return numerator / denominator
    
