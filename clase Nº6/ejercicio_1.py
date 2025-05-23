# ------------------------------------------------------------------------------
# Realizá un programa en Python que permita al usuario ingresar 10 números enteros. El programa debe:

# Almacenar los números ingresados en una lista.

# Calcular la suma de todos los números pares.

# Contar cuántos números impares se ingresaron.

# Mostrar por pantalla:

# La lista completa de números ingresados.

# La suma de los números pares.

# La cantidad de números impares

numeros = []

for i in range(10):
    numero = int(input("Ingrese el núemero: \n"))
    numeros.append(numero)

print(f"La suma de los números es: {sum(numeros)}")

cantidad_pares = 0
cantidad_impares = 0
suma_pares = 0
suma_impares = 0
for n in numeros:
    if n % 2 == 0:
        cantidad_pares += 1
        suma_pares = suma_pares + n
    else:
        cantidad_impares += 1
        suma_impares = suma_impares + n

print(f"La lista completa de número es: {numeros}")
print(f"La cantidad de los números pares es: {cantidad_pares} y la suma es: {suma_pares}")
print(f"La cantidad de números impares es: {cantidad_impares} y la suma es: {suma_impares}")