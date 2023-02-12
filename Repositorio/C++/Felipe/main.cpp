#include <iostream>
#include <conio.h>
#include "funciones.h"
using namespace std;



int main(){
    int n,elec,sum=0;
    cout<<"Bienvenido al prograba de facturacion"<<endl;;
    cout<<"Cuantas facturas va a ingresar"<<endl;
    cin>>n;
    string empresa[n],nombre[n];//Define las listas con la cantidad de facturas que se le pregunto al usuario
    int subtotal[n],totales[n];
    for (int i=0;i<n;i=i+1){//un for que se repite la cantidad de facturas que ingreso el usuario
        string ciclo = "T";//Variable bandera que inicia en T cada vez que se ingresa una nueva factura
        system("cls");
        cout<<"Que empresa esta realizando la facturacion"<<endl;
        cin>>empresa[i];
        cout<<"Nombre de quien esta realizando la factura"<<endl;
        cin>>nombre[i];
        while (ciclo=="T"){//ciclo while que se repite mientras la variable bandera sea T
            system("cls");
            cout<<"Elige el numero de la opcion que buscas"<<endl<<"Recuerda mirar todas las opciones antes de salir"<<endl<<"1) Ingresar Producto"<<endl<<"2) Factura"<<endl<<"3) Totales de IVA"<<endl<<"4) Salir"<<endl;//Opciones del Menu
            cin>>elec;
            switch (elec){
            case 1:
                system("cls");
                llenado();//funcion para ingresar productos
                subtotal[i] = subtotalf();//Funcion que da el valor del subtotal en segundo plano
                break;
            case 2:
                system("cls");
                facturar(empresa,nombre,i);//funcion para ver todos los productos con sus precios individuales, precios totales y la suma de estos
                getch();
                break;
            case 3:
                system("cls");
                total(empresa,nombre,subtotal,i);//funcion que imprime la factura incluyendo IVA descuento y guarda el total de la factura
                getch();
                break;
            case 4:
                ciclo="F";//cambia la variable bandera a F para que ya no ejecute mas el menu
                totales[i]=totalf(subtotal,i);
                break;
            default:
                break;
            }
        }
    }
    for(int i = 0; i < n;i++){//imprime la empresa, el nombre y el precio total de cada factura
        cout<<"Factura: #"<<i+1<<"\nEmpresa: "<<empresa[i]<<"\nFacturador: "<<nombre[i]<<"\nTotal: "<<totales[i]<<"\n===============\n";
        sum = sum + totales[i];//suma el total de todas las facturas
    }
    cout<<"La suma total de todas las facturas: "<<sum;
    cout<<"\n\nFin Del Programa";
    getch();
}

