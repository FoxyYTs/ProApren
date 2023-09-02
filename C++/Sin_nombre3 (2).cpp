#include <iostream>
using namespace std;

main(){
    int num1, num2;
    cout<<"Ingrese un numero: ";
	cin>>num1;
	cout<<"Ingrese otro numero: ";
	cin>>num2;
	if(num1 > num2){
		cout<<"la suma de estos numeros es " << num1+num2;
	}else{
		if(num1==num2){
			cout<<"Los 2 son iguales";
		}else{
			cout<<"la resta de sus numeros es " << num1-num2;
		}
	}	
}