Algoritmo Pico_y_Placa_por_numero_de_Placa
	
	definir dia Como Caracter
	Definir placa, dian Como Entero
	
	Escribir "Dijite Su primer numero de placa"
	leer placa
	
	Segun placa Hacer
		6 o 3:
			Escribir "Su Moto No puede Circular los dias lunes"
		9 o 8:
			Escribir "Su Moto No puede Circular los dias Martes"
		4 o 5:
			Escribir "Su Moto No puede Circular los dias Miercoles"
		7 o 1:
			Escribir "Su Moto No puede Circular los dias Jueves"
		2 o 0:
			Escribir "Su Moto No puede Circular los dias Viernes"
		De Otro Modo:
			Escribir "No a dijitado un caracter valido"
	Fin Segun
FinAlgoritmo
