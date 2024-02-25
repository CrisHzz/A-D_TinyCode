# Calcule la suma de los números impares por un lado y los números pares por otro entre dos números enteros dados (suponga que el primero es menor que el segundo, e incluya los números extremos en la suma)


def sumaParesImpares(number1, number2):
    # Aqui estamos validando que si number1 es mayor que number2, pues para que no se petatee la ram por el Stack Overflow
    if number1 > number2:
        # Esto es un caso base, porque aqui validamos si number1 es igual a number2
        if number1 == number2:
            # Aqui cuando son iguales, validamos si number1 es par o impar
            if number1 % 2 == 0:
                # Aqui retornamos una tupla con el valor de number1 y 0
                return number1, 0
            # Aqui lo mismo que en el if de arriba, validamos si number2 es par o impar
            else:
                # Aqui lo mismo, retornamos una tupla con el valor de 0 y number2
                return 0, number1
        else:
            # Aqui validamos que number1 sea par y si no lo es se ira por el else
            if number1 % 2 == 0:
                # Aqui hacemos el llamado recursivo de la funcion, pero le restamos 1 a number1 para que en cada iteracion esta se vaya acercando cada vez mas a number2 y le pasamos tambien el number2
                pares, impares = sumaParesImpares(number1 - 1, number2)
                # Aqui retornamos una tupla con la suma de number1 y pares, y el valor de impares
                return number1 + pares, impares
            else:
                # Aqui hacemos el llamado recursivo de la funcion, pero le restamos 1 a number1 para que en cada iteracion esta se vaya acercando cada vez mas a number2 y le pasamos tambien el number2
                pares, impares = sumaParesImpares(number1 - 1, number2)
                # Aqui es lo mismo pero en vez de sumar number1 con pares, lo hacemos con impares
                return pares, number1 + impares
    # Se hira por el aqui si number1 no es mayor que number2
    else:
        # Esto es un caso base, porque aqui validamos si number1 es igual a number2
        if number1 == number2:
            # Aqui cuando son iguales, validamos si number1 es par o impar
            if number1 % 2 == 0:
                # Aqui retornamos una tupla con el valor de number1 y 0
                return number1, 0
            # Aqui lo mismo que en el if de arriba, validamos si number2 es par o impar
            else:
                # Aqui lo mismo, retornamos una tupla con el valor de 0 y number2
                return 0, number1
        else:
            # Aqui validamos que number1 sea par y si no lo es se ira por el else
            if number1 % 2 == 0:
                # Aqui hacemos el llamado recursivo de la funcion, pero le sumamos 1 a number1 para que en cada iteracion esta se vaya acercando cada vez mas a number2 y le pasamos tambien el number2
                pares, impares = sumaParesImpares(number1 + 1, number2)
                # Aqui retornamos una tupla con la suma de number1 y pares, y el valor de impares
                return number1 + pares, impares
            else:
                # Aqui hacemos el llamado recursivo de la funcion, pero le sumamos 1 a number1 para que en cada iteracion esta se vaya acercando cada vez mas a number2 y le pasamos tambien el number2
                pares, impares = sumaParesImpares(number1 + 1, number2)
                # Aqui es lo mismo pero en vez de sumar number1 con pares, lo hacemos con impares
                return pares, number1 + impares


number1 = int(input("Ingresa un número: "))
number2 = int(input("Ingresa un número: "))

pares, impares = sumaParesImpares(number1, number2)

print("La suma de los números pares es: ", pares)
print("La suma de los números impares es: ", impares)
