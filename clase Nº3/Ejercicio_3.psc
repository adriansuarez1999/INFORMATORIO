Algoritmo ejercicio_3
	definir usuario, contrase�a como cadena
	definir intentos Como Entero
	intentos = 3
	Mientras intentos > 0  Hacer
		Escribir "ingrese su usuario"
		Leer usuario
		Escribir "Ingrese su contrase�a"
		Leer contrase�a
		
		//usuario va a ser = admin y contrase�a = 1234
		si usuario = "admin" y contrase�a = "1234" Entonces
			Escribir "usuario y contrase�a correctos. BIENVENIDO!!"
			intentos = 0
		SiNo
			Escribir "usuario o contrase�as incorrectas"
			intentos = intentos-1
			si intentos == 0 Entonces
				Escribir "Limite de intentos superados..."
			FinSi
		FinSi
		
	Fin Mientras
	
FinAlgoritmo
