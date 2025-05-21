#Ejercicio 1: Gestión de una lista de compras
#Crea una lista vacía llamada lista_compras
#Luego:
#1- Agregá 3 productos usando .append()
#2- Mostrá cuántos productos hay con len()
#3- Eliminá el último producto con .pop()
#4- Mostrá la lista actualizada
#El objetivo es aprender .append(), .pop() y .len()

lista_compras = []

lista_compras.append("Ananá")
lista_compras.append("Frutilla")
lista_compras.append("Banana")

print(f"La cantidad de productos es: {len(lista_compras)}")

print(f"Ultimo elemento eliminado... {lista_compras.pop(2)}")

print(f"La lista actualizada es: {lista_compras}")