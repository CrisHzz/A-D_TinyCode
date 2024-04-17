#hallamos relacion de la progresion [6, -18, 54, -162] hallamos la razon de cambio:
#"r" = -18/6 = 54/-18 = -162/54 = -3
#con ello ya podemos tener la ecuacion: an = (-3) * an-1 pues necesitamos conocer la posicion anterior
#entonces como termino inicial a1 tenemos el 6


#hallamos la formula no recursiva tenemos que r = -3 y tenemos que a1 = 6
#simplemente tendriamos como formula general de la progrecion a: an = a1 * (-3)**n-1

def progeNoRecursive(n):
    an = [6]
    r = -3

    for i in range(2, n+1):
        an.append(an[0] * (r**(i-1)))

    return an


def progreRecursive(n, a=[6], r=-3):
    if n == 1:
        return a
    else:
        a.append(r * a[-1])
        return progreRecursive(n-1, a, r)


ans = ""
while ans != "r" and ans != "s":
    ans = str.lower(input("Escriba (R) para trabajar de forma recursiva o (S) para trabajar de forma no recursiva"))
    if ans == "r":
        n = int(input("Digite cantidad de posiciones que desee conocer: "))
        result = progreRecursive(n)
        print("El resultado es: ", result)
    elif ans == "s":
        n = int(input("Digite cantidad de posiciones que desee conocer: "))
        result = progeNoRecursive(n)
        print("El resultado es: ", result)
    else:
        print("Digite una opcion valida")


#Primera diferencia (Complejidad temporal):
#Recursiva: La implementación recursiva puede tener una complejidad temporal mayor debido a la sobrecarga de
# llamadas recursivas y la necesidad de calcular términos anteriores repetidamente.
#No recursiva: La implementación no recursiva suele tener una complejidad temporal más baja ya que solo se calcula cada término una vez.

#Segunda diferencia (Uso de memoria):
#Recursiva: La implementación recursiva puede requerir más memoria debido a la pila de llamadas recursivas que debe mantenerse en la memoria.
#No recursiva: La implementación no recursiva generalmente requiere menos memoria ya que no hay necesidad de mantener una pila de llamadas recursivas.

#Tercera diferencia (Facilidad de comprensión y mantenimiento):
#Recursiva: La implementación recursiva puede ser más fácil de entender para algunas personas, especialmente si están familiarizadas con la recursión.
# Sin embargo, puede ser más difícil de depurar y mantener en algunos casos.
#No recursiva: La implementación no recursiva puede ser más directa y fácil de seguir para algunas personas,
# ya que utiliza un enfoque más lineal. Esto puede hacer que sea más fácil de depurar y mantener en algunos casos.
