numeros = []

while True:
    n = float(input("Ingresa un número (negativo para terminar): "))
    if n < 0:
        break
    numeros.append(n)

if numeros:
    print("Número mayor:", max(numeros))
    print("Número menor:", min(numeros))
else:
    print("No se ingresaron números.")
