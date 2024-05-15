def min_cambio(vueltas):
    monedas = [1, 5, 10, 25, 50]
    min_monedas = [0] * (vueltas + 1)

    for i in range(vueltas + 1):
        conteoMonedas = i
        for j in [m for m in monedas if m <= i]:
            if min_monedas[i - j] + 1 < conteoMonedas:
                conteoMonedas = min_monedas[i - j] + 1
        min_monedas[i] = conteoMonedas
    return min_monedas[vueltas]


valor = int(input("ingrese el valor a pagar: "))
pago = int(input("ingrese con cuanto va a pagar: "))
vueltas = pago - valor
min_vueltas = min_cambio(vueltas)
print(f"El valor minimo de vueltas es: {min_vueltas}")
