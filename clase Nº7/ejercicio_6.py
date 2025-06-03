#Crear un set/conjunto con los números impares del 1 al 10 y mostrar el
#número de elementos en el conjunto.

conjunto_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = []

for i in conjunto_numeros:
    if i % 2 > 0:
        numeros_impares.append(i)
print(f"El número de elementos en el conjunto es: {len(numeros_impares)}")