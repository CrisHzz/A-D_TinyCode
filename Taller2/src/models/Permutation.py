from Operation import Operation

class Permutation(Operation):


    def circular_Permutation(self)->int:

        return Permutation.classicFactorial(self.n-1)
    


    def ordinary_operation(self):

        down_equation=Operation.classicFactorial(self.n-self.r)

        return Operation.classicFactorial(self.n)/down_equation



    def variation_operation(self):
        numerator = self.classicFactorial(self.n)

        denominator = 1

        for variable in self.variables:

            denominator *= self.classicFactorial(variable)

        return numerator / denominator
        

        


