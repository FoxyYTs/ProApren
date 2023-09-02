#include <iostream>
using namespace std;

main(){
	double suma, promedio, nota, alumnos;
	cout<<"Cuantos alumnos va a ingresar? : ";
	cin>>alumnos;
	for(int j=0;j<alumnos;j++){
		cout<<"Estudiante numero: "<<j+1<<"\n";
		suma = 0;
		for(int i=0;i < 3; i++){
			cout<<"ingrese su nota querido: ";
			cin>>nota;
			suma += nota;
		}
		promedio = suma/3;
		cout<<"Su promedio es "<< promedio <<"\n";
		
		if(promedio>=3){
			cout<<"usted a aprovado\n";
		}else{
			cout<<"Usted a reprobado\n";
		}
	}
}