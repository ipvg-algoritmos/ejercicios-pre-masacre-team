matriz = []

print("Ingrese 9 números enteros para la matriz 3x3:")

for i in range(3):
    fila = []
    for j in range(3):
        num = int(input())
        fila.append(num)
    matriz.append(fila)

positivos = 0
negativos = 0
ceros = 0
suma_diag_principal = 0
suma_diag_secundaria = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j] > 0:
            positivos += 1
        elif matriz[i][j] < 0:
            negativos += 1
        else:
            ceros += 1

        if i == j:
            suma_diag_principal += matriz[i][j]
        if i + j == 2:
            suma_diag_secundaria += matriz[i][j]

if suma_diag_principal > suma_diag_secundaria:
    print("La suma de la diagonal principal es mayor que la diagonal secundaria.")
elif suma_diag_principal < suma_diag_secundaria:
    print("La suma de la diagonal principal es menor que la diagonal secundaria.")
else:
    print("La suma de la diagonal principal es igual a la diagonal secundaria.")

print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
print("Cantidad de ceros:", ceros)
