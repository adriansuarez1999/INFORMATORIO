Algoritmo login_simulado
	definir usuario, contraseña como cadena
	definir intentos Como Entero
	intentos = 3
	Mientras intentos > 0  Hacer
		Escribir "ingrese su usuario"
		Leer usuario
		Escribir "Ingrese su contraseña"
		Leer contraseña
		
		//usuario va a ser = admin y contraseña = facil123
		si usuario = "admin" y contraseña = "facil123" Entonces
			Escribir "usuario y contraseña correctos. BIENVENIDO!!"
			intentos = 0
		SiNo
			Escribir "usuario o contraseñas incorrectas"
			intentos = intentos-1
		FinSi
	Fin Mientras
	Escribir "Limite de intentos superados..."
FinAlgoritmo
