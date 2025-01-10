Algoritmo sin_titulo
	Definir dia Como Caracter
	Definir placa Como Entero
	Escribir 'Dijite el dia que quiere consultar'
	Leer dia
	Escribir 'Dijite el numero de placa que quiere consultar'
	Leer placa
	Segun dia  Hacer
		'Lunes','lunes','LUNES':
			Si placa=6 O placa=3 Entonces
				Escribir 'Su vehiculos no puede conducir los dias ',dia
			SiNo
				Escribir 'Los ',dia,' los vehiculos que comiences por 6 o 3 no pueden circular'
			FinSi
		'Martes','martes','MARTES':
			Si placa=9 O placa=8 Entonces
				Escribir 'Su vehiculos no puede conducir los dias ',dia
			SiNo
				Escribir 'Los ',dia,' que comiences por 9 o 8 no pueden circular'
			FinSi
		'Miercoles','miercoles','MIERCOLES':
			Si placa=4 O placa=5 Entonces
				Escribir 'Su vehiculos no puede conducir los dias ',dia
			SiNo
				Escribir 'Los ',dia,' que comiences por 4 o 5 no pueden circular'
			FinSi
		'Jueves','jueves','JUEVES':
			Si placa=7 O placa=1 Entonces
				Escribir 'Su vehiculos no puede conducir los dias ',dia
			SiNo
				Escribir 'Los ',dia,' que comiences por 7 o 1 no pueden circular'
			FinSi
		'Viernes','viernes','VIERNES':
			Si placa=2 O placa=0 Entonces
				Escribir 'Su vehiculos no puede conducir los dias ',dia
			SiNo
				Escribir 'Los ',dia,' que comiences por 2 o 0 no pueden circular'
			FinSi
		'Sabado','sabado','SABADO','Domingo','domingo','DOMINGO':
			Escribir 'Hoy no hay restricciones'
		De Otro Modo:
			Escribir 'No a dijitado un caracter valido'
	FinSegun
FinAlgoritmo
