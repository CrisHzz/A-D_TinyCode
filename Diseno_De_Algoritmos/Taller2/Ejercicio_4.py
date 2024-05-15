# Todas las sumas en vertical y horizontal deben dar el mismo resultado (14)


def sumas_iguales_backtrack(matriz, suma=0, suma2=0):
    n = len(matriz)
    if suma == 14:
        return "La suma de la fila no es 14"
    else:
        for i in range(n):
            suma += matriz[0][i]
            print(suma)
            if suma == 14:
                for j in range(n):
                    suma2 += matriz[j][0]
                    print(suma2)
            else:
                return "No se puede"
    # return sumas_iguales_backtrack(matriz, suma)


matriz = [[1, 10, 3], [4, 5, 6], [4, 1, 2]]

sumas_iguales_backtrack(matriz)


# Profe, no me dio el Ki
