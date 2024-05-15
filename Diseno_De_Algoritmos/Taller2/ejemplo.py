def backtrack(permutacion_actual, elementos_restantes):
    # Caso base: si no quedan elementos por permutar, imprime la permutación actual
    if not elementos_restantes:
        print(permutacion_actual)
    else:
        # Para cada elemento restante, realiza backtracking
        for i in range(len(elementos_restantes)):
            # Selecciona un elemento y lo agrega a la permutación actual
            siguiente_elemento = elementos_restantes[i]
            permutacion_actual.append(siguiente_elemento)
            # Actualiza la lista de elementos restantes
            elementos_restantes_actualizados = elementos_restantes[:i] + elementos_restantes[i+1:]
            # Realiza backtracking con la permutación actualizada
            backtrack(permutacion_actual, elementos_restantes_actualizados)
            # Retrocede: elimina el último elemento agregado para probar otras combinaciones
            permutacion_actual.pop()

# Ejemplo de uso
lista = [1, 2, 3]
backtrack([], lista)
