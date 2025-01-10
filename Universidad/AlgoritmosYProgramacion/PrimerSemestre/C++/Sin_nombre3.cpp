#include <iostream>
using namespace std;

main(){
	int lista[5];
	for (int i = 0; i < 5; i++){
		cout<<"ingresa un numero: ";
		cin>>lista[i];
	}
	for (int i = 0; i < 10; i++){
		cout<<"\nEn la pocicion "<<i<<" esta el: "<<lista[i];
	}
	
}