#include <iostream>
#include<math.h>
// NOTA: 4,9. Felicitaciones

//1. El ejercicio muestra un resultado pero no se dice de que es, o sea resutado: 

using namespace std;

main(){
   
	//Ejercicio 1
	int x = 5,y = 14,r;
	//"X" y "Y" variables dadas por el taller
	// "r" es donde se almacena el resultado de la operacion
	// Pow es de la libreria math que sirve para hacer potencias
	r = (pow(7,x))/7+(x*20)-y+25;
    cout<<r<<"\n";
    cout<<"Fin del programa";
    
    
    
    //Ejercicio 2
    float pesos, dolares, valor = 4400;
    int op;
    //"pesos" y "dolares" es la cantidad que el usuario quiere convertir de su respectiva divisa
    //"op" es la la variable para saber que procedimiento elegir
    //"valor" es el valor de 1 dolar en pesos
    cout<<"Que proceso desea realizar ?\n1 = Un cambio de Pesos a Dolares\n2 = Un cambio de Dolares a Pesos\nIngrese el numero de la opcion que eligio: ";
    cin>> op;
    switch(op){
    	case 1:
    		//Esta es la opcion para transformar Pesos a Dolares, esta divide la cantidad de Pesos que elija el usuario entre el valor actual del dolar en pesos y el resultado es la cantidad en Dolares
	    	cout<<"Usted a elegido de Pesos a Dolares\nahora ingrese la cantidad: ";
	    	cin>> pesos;
	    	cout<<"El cambio es "<<(pesos/valor);
	    	break;
    	case 2:
    		//Esta es la opcion para transformar Dolares a pesos, esta multiplica la cantidad de Dolares que elija el usuario entre el valor actual del dolar en pesos y el resultado es la cantidad en Pesos
			cout<<"Usted a elegido de Dolares a Pesos\nahora ingrese la cantidad: ";
			cin>> dolares;
			cout<<"El cambio es "<<(dolares*valor);
			break;
		default:
			//Esta opcion es para cuando el usuario no dijita una opcion valida
			cout<<"No a elegino una opcion valida";
	}
	cout<<"\nFin del programa";
}
