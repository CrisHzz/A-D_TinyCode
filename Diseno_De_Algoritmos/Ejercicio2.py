def min_operator(n: int):
    if n == 0:
        return 0

    if n % 2 == 0:
        return min_operator(n // 2) + 1

    return 1 + min_operator(n // 2) + 1


n = int(input("Digite el valor para N: "))
print(min_operator(n)-1)
