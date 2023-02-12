#include <iostream>
#include <string>
using namespace std;

//facturar 3 productos e imprimit el todal, subtotal y los datos

int main(){

    int total = 0,n=0,subtotal=0,descuento = 0,cedula,ultimototal=0,iva=0;
    string terminar="si";

    cout<<"Hola Me llamo Facturadora de productos";
    for (int x = 0; terminar == "si"; x++){
        cout<<"\nNumero de cedula: ";
        cin>>cedula;
        cout<<"\nCuantos productos quieres facturar: ";
        cin>>n;
        cin.ignore( );
        int valor_unidad[n],cantidad[n],valor_producto[n];
        string producto[n]; 
        for(int i=0;i<n;i++){
            cout<<"\n========================================\ningrese el nombre del pruducto: ";
            getline(cin, producto[i]);
            cout<<"\nIngrese el valor de la unidad: ";
            cin>>valor_unidad[i];
            cout<<"\ningrese la cantidad: ";
            cin>>cantidad[i];
            //ignore(), limpia el buffer y los saltos de linea
            cin.ignore( );
            valor_producto[i]=valor_unidad[i]*cantidad[i];
            subtotal=subtotal+valor_producto[i];
            if(subtotal > 50000){
                descuento=subtotal*0.10;
                total = subtotal - descuento;
            }
            iva = total*0.19;
            ultimototal=total+iva;
        }
        for(int j=0;j<n;j++){
            cout<<"\n========================================\nProducto"<<j+1<<": "<<producto[j]<<"\nValor: "<<valor_unidad[j]<<"\nCantidad: "<<cantidad[j]<<"\nSubtotal: "<<valor_producto[j];
        }
        cout<<"\n========================================\nIdentificacion: "<<cedula<<"\nsubtotal: "<<subtotal<<"\nTotal con descuento: "<<total<<"\niva: "<<iva<<"\nValor Final: "<<ultimototal<<"\nFin del Programa";
        cout<<"\n========================================\ndeseas continuar?\nContinuar=si/Cerrar=no: ";
        cin>>terminar;
        return 0;
        }  
}