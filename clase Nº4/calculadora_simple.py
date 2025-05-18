print("--Calculadora simple--")

numero1 = int(input("Ingrese un número: \n"))
caracter = input("Ingrese la operación (+,-,*,/): \n")
numero2 = int(input("Ingrese un segundo número: \n"))


if caracter == "+":
    print(f"La suma es:\n {numero1} + {numero2} = {numero1+numero2}")
elif caracter == "-":
    print(f"La resta es:\n {numero1} - {numero2} = {numero1-numero2}")
elif caracter == "*":
    print(f"La multiplicación es:\n {numero1} * {numero2} = {numero1*numero2}")
elif caracter == "/":
    if numero2 != 0:
        print(f"La división es:\n {numero1} / {numero2} = {numero1/numero2}")
    else:
        print("No se puede dividir por cero")
else:
    print("No se puede realizar la operación")
