# Punto Numero 1
# Resolver la siguiente relación de recurrencia entregando la recurrencia sin recursividad y su ecuación particular según las condiciones de frontera:

from colorama import init

init()
import decimal

a_0 = 6
a_1 = 5

r = 3


def recurrencia(n):
    a_n = decimal.Decimal(6) * decimal.Decimal(3) ** decimal.Decimal(
        n
    ) + decimal.Decimal(-13 / 3) * decimal.Decimal(n) * decimal.Decimal(
        3
    ) ** decimal.Decimal(
        n
    )
    return a_n


print(
    "\033[93;1m"
    + "El resultado del primer punto es: "
    + "\033[0m"
    + "\033[91;1m"
    + str(recurrencia(1500))
    + "\033[0m"
)

# Resultado -3.121722997276988324624596315E+719

# Punto Numero 2
# Escribir una función recursiva que encuentre los valores repetidos de una lista


def repetidos(lista):
    if len(lista) == 0:
        return []
    if lista[0] in lista[1:]:
        return [lista[0]] + repetidos(lista[1:])
    return repetidos(lista[1:])


lista = [1, 2, 2, 3, 1, 2, 4, 3]
print(
    "\033[93;1m"
    + "El resultado del segundo punto es: "
    + "\033[0m"
    + "\033[91;1m"
    + str(repetidos(lista))
    + "\033[0m"
)

# Punto Numero 3
# Se tienen 10 libros de poesía y 7 libros de novela. ¿Cuántos conjuntos diferentes de 4 libros pueden formarse si al menos 2 deben ser libros de poesía?

# primero encontrar al menos 2 libros de poesía
# Combinatoria sin repetición
# n! / r! * (n - r)!

# 10!/(10-2)! * 2! = 45

# 17!/(17-4)! * 4! = 2380

# 45 * 2380 = 107100 Es la cantidad de formas que se pueden combinar
