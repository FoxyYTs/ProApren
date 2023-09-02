#include <iostream>
#include <conio.h>
#include "funcion.h"
using namespace std;



main(){
    int n,eleccion,suma;
    cout<<"Inicio del programa para facturar\n";
    cout<<"Cuantas facturas van a procesar: ";
    cin>>n;
    string nombreEmp[n],nombreFac[n];
    int subtotal[n],totales[n];
    for (int i = 0 ; i < n ; i++){
        bool ciclo = true;
        system("cls");
        cout<<"De que empresesa es esta factura: ";
        cin>>nombreEmp[i];
        cout<<"Nombre del facturador: ";
        cin>>nombreFac[i];
        do{
            system("cls");
            cout<<"Elige el numero de la opcion que buscas";
            cout<<"\n1- Ingresar Producto";
            cout<<"\n2- Factura";
            cout<<"\n3- Totale de IVA";
            cout<<"\n4- Terminar esta factura";
            cout<<"\nEleccion: ";
            cin>>eleccion;
            if(eleccion == 1){
                system("cls");
                llenar(nombreEmp,nombreFac,i);
                totales[i] = totaldiscreto();
            }else if(eleccion == 2){
                system("cls");
                facturar();
                getch();
            }else if(eleccion == 3){
                system("cls");
                total();
                getch();
            }else if(eleccion == 4){
                ciclo = false;
            }else{
                cout<<"opcion no valida";
            }
        }while (ciclo);
    }
    suma = sumfacturas(nombreEmp,nombreFac,totales,n);
    cout<<"\n----------------------------------------";
    cout<<"\nLa suma de todas las facturas es: "<<suma;
    cout<<"\n\nFinal";
    getch();    
}