#include <iostream>
#include <string>
using namespace std;

//facturar 3 productos e imprimit el todal, subtotal y los datos

int main(){

    int total = 0, subtotal, valor_unidad[3],cantidad[3],valor_producto[3];
    string producto[3];

    cout<<"Hola Me llamo Facturadora de productos";
    for(int i=0;i<3;i++){
        cout<<"\n========================================\ningrese el nombre del pruducto: ";
        getline(cin, producto[i]);
        cout<<"\nIngrese el valor de la unidad: ";
        cin>>valor_unidad[i];
        cout<<"\ningrese la cantidad: ";
        cin>>cantidad[i];
        //ignore(), limpia el buffer y los saltos de linea
        cin.ignore( );
        valor_producto[i]=valor_unidad[i]*cantidad[i];
        total=total+valor_producto[i];
    }
    for(int j=0;j<3;j++){
    	cout<<"\n========================================\nProducto"<<j+1<<": "<<producto[j]<<"\nValor: "<<valor_unidad[j]<<"\nCantidad: "<<cantidad[j]<<"\nSubtotal: "<<valor_producto[j];
	}
    cout<<"\n========================================\ntotal: "<<total<<"\nFin del Programa";

    return 0;
}