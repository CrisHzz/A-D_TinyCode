# Calcule la suma de los números impares por un lado y los números pares por otro entre dos números enteros dados (suponga que el primero es menor que el segundo, e incluya los números extremos en la suma)


def sumaParesImpares(number1, number2):  # O(n)
    if number1 > number2:  # O(0)
        # Esto es un caso base, porque aqui validamos si number1 es igual a number2
        if number1 == number2:  # O(0)
            if number1 % 2 == 0:  # O(0)
                # Aqui retornamos una tupla con el valor de number1 y 0
                return number1, 0  # O(0)
            else:  # O(0)
                # Aqui lo mismo, retornamos una tupla con el valor de 0 y number2
                return 0, number1  # O(0)
        else:  # O(0)
            if number1 % 2 == 0:  # O(0)
                # Aqui hacemos el llamado recursivo de la funcion, pero le restamos 1 a number1 para que en cada iteracion esta se vaya acercando cada vez mas a number2 y le pasamos tambien el number2
                pares, impares = sumaParesImpares(number1 - 1, number2)  # O(n)
                return number1 + pares, impares  # O(0)
            else:  # O(0)
                # Aqui hacemos el llamado recursivo de la funcion, pero le restamos 1 a number1 para que en cada iteracion esta se vaya acercando cada vez mas a number2 y le pasamos tambien el number2
                pares, impares = sumaParesImpares(number1 - 1, number2)  # O(n)
                return pares, number1 + impares  # O(0)
    else:  # O(0)
        # Esto es un caso base, porque aqui validamos si number1 es igual a number2
        if number1 == number2:  # O(0)
            if number1 % 2 == 0:  # O(0)
                # Aqui retornamos una tupla con el valor de number1 y 0
                return number1, 0  # O(0)
            else:  # O(0)
                # Aqui lo mismo, retornamos una tupla con el valor de 0 y number2
                return 0, number1  # O(0)
        else:  # O(0)
            if number1 % 2 == 0:  # O(0)
                # Aqui hacemos el llamado recursivo de la funcion, pero le sumamos 1 a number1 para que en cada iteracion esta se vaya acercando cada vez mas a number2 y le pasamos tambien el number2
                pares, impares = sumaParesImpares(number1 + 1, number2)  # O(n)
                return number1 + pares, impares  # O(0)
            else:  # O(0)
                # Aqui hacemos el llamado recursivo de la funcion, pero le sumamos 1 a number1 para que en cada iteracion esta se vaya acercando cada vez mas a number2 y le pasamos tambien el number2
                pares, impares = sumaParesImpares(number1 + 1, number2)  # O(n)
                return pares, number1 + impares  # O(0)


number1 = int(input("Ingresa un número: "))  # O(0)
number2 = int(input("Ingresa un número: "))  # O(0)

pares, impares = sumaParesImpares(number1, number2)  # O(n)

print("La suma de los números pares es: ", pares)  # O(0)
print("La suma de los números impares es: ", impares)  # O(0)

# Entonces la complejidad total del algoritmo es: 26 O(n) + 5 O(n) = O(n)