numeros = [15, 7, 23, 4, 9, 1, 30, 12, 18, 6]

print("Mi lista es:", numeros)

buscar = int(input("¿Qué número quieres encontrar? "))

hallado = False

for i in range(len(numeros)):
    if numeros[i] == buscar:
        print(f"¡Sí! El número {buscar} está en la posición {i + 1}.")
        hallado = True
        break 

if not hallado:
    print(f"El número {buscar} no está en la lista.")