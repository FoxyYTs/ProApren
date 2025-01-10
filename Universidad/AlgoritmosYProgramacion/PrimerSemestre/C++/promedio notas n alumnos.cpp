#include <iostream>

using namespace std;

main(){
	int nalum;
	float nota, notas, promedio, promedios, tp;
	string nombre;
	
    cout<<"Cuantos estudiantes va a evaluar?\nEstudiantes: ";
    cin>>nalum;
    for(int i = 0;i<nalum;i++){
    	cout<<"================================================================================\n";
    	notas = 0;
    	cout<<"Dijite su nombre: ";
    	cin>>nombre;
    	cout<<"Vamos a sacar el promedio de sus 3 notas, porfavor dijitelas 1 por 1\n";
    	for(int j = 0;j<3;j++){
    		cout<<"Dijite su nota: ";
    		cin>>nota;
    		notas += nota;
    		promedio = notas/3;
		}
		cout<<"El promedio del estudiante "<< nombre<<" es "<<promedio<<"\n";
		if (promedio < 3){
			cout<<"Usted a Reprovado\n";
		}else if(promedio >= 3){
			cout<<"Usted a aprovado\n";
		}
		promedios += promedio;
		tp = promedios / nalum;
	}
	cout<<"La suma de las notas de todos los estudiantes es "<<promedios<<"\n";
	cout<<"El promedio entre todos los alumnos es "<<tp;
}
