#Escribir un programa que lea un entero positivo, n, introducido 
# por el usuario y después muestre en pantalla la suma de todos los 
# enteros desde 1 hasta n.

n = int(input("Ingrese un número entero: "))

suma_enteros = n*(n+1)/2

print(f"La suma de los números anteriores a {n} es: {int(suma_enteros)}")