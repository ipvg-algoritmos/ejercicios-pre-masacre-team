texto = input("Escribe un texto: ")

vocales = "aeiouAEIOU"
v = 0
c = 0

for letra in texto:
    if letra.isalpha():
        if letra in vocales:
            v += 1
        else:
            c += 1

print("Vocales:", v)
print("Consonantes:", c)
