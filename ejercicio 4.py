suma_total = 0
cantidad_numeros = 0

print("Por favor, ingresa números para calcular su promedio.")
print("Cuando quieras terminar, ingresa un número negativoo.")

while True:
    try:
        numero_ingresado = float(input("Ingresa un número: "))

        if numero_ingresado < 0:
            break  
        
        suma_total += numero_ingresado
        cantidad_numeros += 1
    except ValueError:
        print("¡Error! Eso no es un número válido. Inténtalo de nuevo.")

if cantidad_numeros > 0:
    promedio = suma_total / cantidad_numeros
    print(f"\nHas ingresado {cantidad_numeros} números.")
    print(f"La suma total es: {suma_total}")
    print(f"El promedio de los números ingresados es: {promedio:.2f}") 
else:
    print("\nNo ingresaste ningún número válido para calcular el promedio.")