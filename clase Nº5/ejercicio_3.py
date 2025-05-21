# Ejercicio 3: Diccionario de estudiante
# Dado este diccionario:
# estudiante = {
#  "nombre": "Ana",
#  "edad": 20,
#  "materias": ["Matemática", "Historia"]
# }
# 1- Mostrá el nombre y la edad
# 2- Agregá una materia nueva a la lista materias
# 3- Mostrá cuántas materias cursa con len()
# 4- Usá .get() para obtener la clave “promedio” con valor por defecto 0
# El objetivo es obtener acceso al diccionario, lista dentro de diccionario y aprender .get() y len()

estudiante = {
  "nombre": "Ana",
  "edad": 20,
  "materias": ["Matemática", "Historia"]
}

print(f"El nombre es: {estudiante["nombre"]} \nLa edad es: {estudiante["edad"]} años")

print("Agregando una nueva materia...")
estudiante["materias"].append("Ingles")

print(f"La cantidad de materias que cursa es: {len(estudiante["materias"])}")