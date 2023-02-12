#include <iostream>
using namespace std;

main(){
	int person,eleccion,precio,iva,total,subtotal,cantidad,finalcant=0;
	cout<<"Cuantas personas van a pedir: ";
	cin>>person;
	for(int i = 0; i<person;i++){
		cout<<"==============================================";
		cout<<"\nEl Menu del dia es: \n\n1) Bandeja paisa = $15k \n2) Sancocho = $12k \n3) Mondongo = $14k \n4) Consome = $8k \n\nDijite el numero de lo que quiere: ";
		cin>>eleccion;
		if(eleccion==1){
			cout<<"\nUsted a elegido una Bandeja paisa = $15k";
			cout<<"\nCuantos platos va a pedir: ";
			cin>>cantidad;
			precio=15000*cantidad;
		}else if(eleccion==2){
			cout<<"\nUsted a elegido un Sancocho = $12k";
			cout<<"\nCuantos platos va a pedir: ";
			cin>>cantidad;
			precio=12000*cantidad;
		}else if(eleccion==3){
			cout<<"\nUsted a elegido un Mondongo = $14k";
			cout<<"\nCuantos platos va a pedir: ";
			cin>>cantidad;
			precio=14000*cantidad;
		}else if(eleccion==4){
			cout<<"\nUsted a elegido un Consome = $8k";
			cout<<"\nCuantos platos va a pedir: ";
			cin>>cantidad;
			precio=8000*cantidad;
		}else{
			cout<<"\nA elegijo una opcion no valida, Por favor dijite una opcion valida para continuar";
			i--;
		}
		finalcant=finalcant+cantidad;
		subtotal+=precio;
		total=subtotal+(subtotal*0.10);
		cout<<"\n\nLa cuenta va en: "<<subtotal<<" Mas iva "<<total<<"\n";	
	}
	cout<<"\n\nEl precio final del pedido es: $"<<subtotal<<" Con iva es: $"<<total;
	cout<<"\nEn esta cuenta se pidieron: "<<finalcant<<" platos";
}