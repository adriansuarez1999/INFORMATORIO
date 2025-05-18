Algoritmo ejercicio_3
	definir usuario, contraseña como cadena
	definir intentos Como Entero
	intentos = 3
	Mientras intentos > 0  Hacer
		Escribir "ingrese su usuario"
		Leer usuario
		Escribir "Ingrese su contraseña"
		Leer contraseña
		
		//usuario va a ser = admin y contraseña = 1234
		si usuario = "admin" y contraseña = "1234" Entonces
			Escribir "usuario y contraseña correctos. BIENVENIDO!!"
			intentos = 0
		SiNo
			Escribir "usuario o contraseñas incorrectas"
			intentos = intentos-1
			si intentos == 0 Entonces
				Escribir "Limite de intentos superados..."
			FinSi
		FinSi
		
	Fin Mientras
	
FinAlgoritmo
