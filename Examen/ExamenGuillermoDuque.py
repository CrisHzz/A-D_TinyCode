#Punto1
#7an-1 + 2an + 3an-2 = 0    ->   2x**2 + 7x + 3 = 0
#teniendo la ecuacion cuadratica anterior (haciendo formula del estudiante), tenemos:
#x1 = -1/2
#x2 = -3
#tenemos que an = c1(-1/2)**n + c2(-3)**n
#a0 = #letrasPrimerNombre = 9 y a1 = #letrasPrimerApellido = 5
#9 = c1(-1/2)**0 + c2(-3)**0  -> 9 = c1 + c2
#5 = c1(-1/2)**1 + c2(-3)**1  -> -c1/2 - 3c2
#usando operacion entre matrices tenemos que c1 = 64/5 y c2 = -19/5
#tenemos an = 64/5(-1/2)**n - 19/5(-3)**n
#ahora
import decimal

n = 1500
an = decimal.Decimal(64/5)*decimal.Decimal((-1/2)**n) - decimal.Decimal(19/5)*decimal.Decimal((-3)**n)
print("punto 1: ", an)


#punto2
def find_combinations(digits, current='', index=0, result=[]):
    if index == len(digits):
        result.append(current)
        return

    find_combinations(digits, current + digits[index], index + 1, result)
    find_combinations(digits, current + ' ' + digits[index], index + 1, result)

    for combination in result:
        print(combination)


numero = "123"
print(find_combinations(numero))


#punto3
import math
#A,B,C,D,E,F Y G
# y A,B no pueden estar juntos
# es una permutacion ordinaria cuya operacion es m! = 7!, ahora de esto toca sacar las combinaciones donde A,B estan juntas
# las combinaciones posibles donde a y b estan juntos es 4!
resultado = math.factorial(7) - math.factorial(4)
print("resultado de la permutacion del punto 3 es: ", resultado)
