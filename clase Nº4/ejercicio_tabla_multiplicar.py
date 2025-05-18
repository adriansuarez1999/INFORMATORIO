numero = input("Ingrese el número: ")
print(f"Tabla de multiplicar {numero}:\n")
for i in range(1,11):
    print(f"{numero} X {i} = {i * int(numero)}")