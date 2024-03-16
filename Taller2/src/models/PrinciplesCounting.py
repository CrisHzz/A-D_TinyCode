class PrinciplesCounting(list):
    def __init__(self):
        try:
            input_value = input("Ingrese los valores separados por espacios: ")
            values = map(int, input_value.split())
            if any(value <= 0 or isinstance(value, str) for value in values):
                raise ValueError("Debe ingresar solo números positivos diferentes de cero.")
            super().__init__(map(int, input_value.split()))
        except ValueError:
            print("Error porfavor digite un numero :)")
            self.__init__()

    def list_multiplier(self):
        result = 1
        for value in self:
            result *= value
        return result


input_list = PrinciplesCounting()
print_count_result = input_list.list_multiplier()
print("El resultado de la multiplicación de los valores dentro de la funcion es: ", print_count_result)
