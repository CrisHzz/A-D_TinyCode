# Dada una matriz n*n mostrar el camino mas optimo desde la posicion (0,0) a (n,n), mostrando el valor de la suma de los valores de la matriz en el camino mas optimo


def optimal_path(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("La entrada debe ser una matriz (lista de listas).")
    
    n = len(matrix)
    
    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("La matriz debe ser cuadrada (n x n) y no vacía.")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise ValueError("Todos los elementos de la matriz deben ser números.")
    
    
    # Usaremos memoización para almacenar los resultados ya calculados
    memo = [[None] * n for _ in range(n)]
    
    def find_path(r, c):
        if r == n-1 and c == n-1:
            return [(r, c)], matrix[r][c]
        
        if memo[r][c] is not None:
            return memo[r][c]
        
        # Movimiento solo hacia abajo o hacia la derecha
        down_path, down_cost = find_path(r+1, c) if r+1 < n else (None, float('inf'))
        right_path, right_cost = find_path(r, c+1) if c+1 < n else (None, float('inf'))
        
        # El costo mínimo para llegar a (r,c)
        if down_cost < right_cost:
            path = [(r, c)] + down_path
            total_cost = matrix[r][c] + down_cost
        else:
            path = [(r, c)] + right_path
            total_cost = matrix[r][c] + right_cost
        
        # Guardar el resultado en memo
        memo[r][c] = (path, total_cost)
        
        return memo[r][c]
    
    # Comenzar desde la posición (0,0)
    optimal_path, min_sum = find_path(0, 0)
    
    # Imprimir los elementos del camino más óptimo
    print("El camino más óptimo es:")
    for r, c in optimal_path:
        print(f"({r},{c}): {matrix[r][c]}")
    
    return min_sum

# Ejemplo de uso
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = optimal_path(matrix)
print("La suma mínima de valores en el camino más óptimo es:", result)
