Algoritmo ejercicio_3
	definir usuario, contraseņa como cadena
	definir intentos Como Entero
	intentos = 3
	Mientras intentos > 0  Hacer
		Escribir "ingrese su usuario"
		Leer usuario
		Escribir "Ingrese su contraseņa"
		Leer contraseņa
		
		//usuario va a ser = admin y contraseņa = 1234
		si usuario = "admin" y contraseņa = "1234" Entonces
			Escribir "usuario y contraseņa correctos. BIENVENIDO!!"
			intentos = 0
		SiNo
			Escribir "usuario o contraseņas incorrectas"
			intentos = intentos-1
			si intentos == 0 Entonces
				Escribir "Limite de intentos superados..."
			FinSi
		FinSi
		
	Fin Mientras
	
FinAlgoritmo
