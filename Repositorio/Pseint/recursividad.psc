Funcion fibo ( cN,bN,aN )
	Si aN > 0 Entonces
		Definir dN Como Entero
		dN <- cN + bN
		Escribir cN "+" bN "=" dN
		fibo(dN,cN,aN - 1)
	FinSi
Fin Funcion

Funcion conta ( i )
	Si i > 0 Entonces
		conta(i - 1)
		Escribir i
	Fin Si
Fin Funcion



Algoritmo sin_titulo
	conta(10)
	fibo(1,0,10)
FinAlgoritmo
