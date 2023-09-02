Algoritmo Nomina
	Definir name Como Caracter
	definir h, vh, boni, subtotal, total, trabajador Como Entero
	
	Escribir "Cuantos trabajadores va a evaluar?"
	leer trabajador
	Escribir "Cuanto Valen las horas ?"
	leer vh
	
	Para i<-1 Hasta trabajador Con Paso 1 Hacer
		Escribir "Como se llama el trabajador?"
		leer name
		Escribir "Cuantas horas a trabajado?"
		leer h
		
		subtotal <- h*vh
		
		Si h > 48 Entonces
			boni <- 10000
			Escribir "Pedro a ganado una bonificacion " boni
		SiNo
			bonificacion <- 0
		FinSi
		
		total <- subtotal+boni
		
		Escribir "El trabajador " name " a Ganado " subtotal " mas la bonificacion serian " total
	Fin Para
	
	
FinAlgoritmo
