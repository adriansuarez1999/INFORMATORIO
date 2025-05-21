#Ejercicio 2: Contar apariciones
#Dada la lista:
#colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
#1- Mostrá cuántas veces aparece “rojo” usando .count().
#2- Reemplazá el primer “verde” por “amarillo”
#3- Mostrá la lista final
#El objetivo es usar el método .count(), acceso por índice, asignación de valor. 

colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]

print(f"La cantidad de veces que se repite rojo es: {colores.count("rojo")}")

color_a_reemplazar = colores.index("verde")

print(f"Reemplazando el color verde por amarillo...")
colores[color_a_reemplazar] = "amarillo"

print(f"La lista actualizada es: \n{colores}")