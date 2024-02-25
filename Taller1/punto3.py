a = int(input("Digite el numero base"))
n = int(input("Digite el exponente"))


def elevar_num_base(a: int, n: int):                # primera forma -> O(N)
    resultado = a**n
    return resultado


def eficiente_elevar_num_base(a: int, n: int):          # segunda forma -> O(LOG N)
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a *= a
        n //= 2
    return result


print(f"de forma eficiente: {eficiente_elevar_num_base(a, n)}")
print(f"de forma simple e ineficiente: {elevar_num_base(a, n)}")


# Ambas formas calculan la potencia de un número a elevado a una potencia n, la diferencia principal radica en el enfoque de implementación y eficiencia.


# La segunda forma utiliza un algoritmo de exponenciación binaria, que es altamente eficiente, con complejidad O(Log n) en lugar de O(n)
# Es especialmente útil cuando lidiamos con exponentes grandes, ya que reduce significativamente el número de operaciones.


# La primera forma simplemente utiliza el operador de potencia ** de Python para calcular la potencia de (a) elevado a (n)
# Este método es más simple y directo, pero puede volverse menos eficiente para exponentes grandes debido a la cantidad de operaciones que deben realizarse


# En resumen, mientras que ambas formas dan el mismo resultado, la segunda forma (exponenciación binaria) es preferible cuando se necesita eficiencia,
# especialmente con exponentes grandes. La primera forma (operador de potencia) es más simple y adecuada para casos donde la eficiencia no es crítica o
# para exponentes pequeños.
