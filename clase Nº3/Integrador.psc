Algoritmo integrador
	Definir numero_secreto, numero, intentos Como Entero
	numero_secreto = Aleatorio(1,100)
	intentos = 0
	Mientras intentos < 10 y numero <> numero_secreto Hacer
		Escribir "Ingrese el número"
		Leer numero
		si numero < numero_secreto Entonces
			Escribir "El número secreto es mayor al ingresado. Vuelva a intentarlo"
		SiNo
			si numero > numero_secreto Entonces
				Escribir "El número secreto es menor al ingresado. Vuelva a intentarlo"
			SiNo
				Escribir "Adivinaste el número en ", intentos + 1, " intentos. Felicidades"
			FinSi
		FinSi
		intentos = intentos + 1
	FinMientras
	si numero <> numero_secreto Entonces
		Escribir "Superaste los 10 intentos. El número secreto era ", numero_secreto, ". Suerte para la proxima"
	FinSi
FinAlgoritmo
