#include <iostream>
using namespace std;

int main() {
	int lista[6];
	int inf, supe, mitad, valor=15, cont=0;
	char bandera='f';
	int i,j;
	for(i=0; i<6; i++) {
        cout<<"\nIngrese un numeros: "<<endl;
        cin>>lista[i];
        	
    }
    cout<<"Lista: { ";
    for(int j=0; j<i; j++) {
        cout<<lista[j]<<",  ";
    }
    cout<<"}\n";
	inf=0, supe=6;
	cout<<"\nIngrese un número: ";
	cin>>valor;
	
	while((inf<supe)&&(cont<6)) {
		mitad=(inf+supe)/2;
		if(lista[mitad]==valor) {
			bandera='v';
			break;
		}
		if(lista[mitad]>valor) {
			supe=mitad;
			mitad=(inf+supe)/2;
		}
		if(lista[mitad]<valor) {
			inf=mitad;
			mitad=(inf+supe)/2;
		}
		cont++;
	}
	if(bandera=='v') {
		cout<<"el numero esta en la lista, en la posicion: "<<mitad+1<<endl;
	} else if(bandera=='f') {
		cout<<"el numero no esta en la lista"<<endl ;
	}

	return 0;
}