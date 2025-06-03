#Crear un diccionario con los nombres de tres personas y sus
#respectivas edades. Mostrar la edad de la tercera persona en el
#diccionario.

personas = {"Aithana": "18 años", "Adrian": "26 años", "Roberto": "36 años"}

nombres = list(personas.keys())
print (f"La edad de {nombres[-1]} es: {personas["Roberto"]}")