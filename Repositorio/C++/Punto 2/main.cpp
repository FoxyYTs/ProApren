#include <iostream>
#include <conio.h>
#include "funciones.h"
using namespace std;



int main()
{
    int n,opcion,suma_total_facturas = 0;
    cout<<"Bienvenido al programa de facturacion\n";
    cout<<"dijite el numero de facturas a ingresar: ";
    cin>>n;
    string nombre_compania[n],nombre_trabajador[n];
    int subtotal_facturas[n],total_facturas[n];
    for (int i=0;i<n;i++)
    {
        string bandera = "T";
        system("cls");
        cout<<"Cual es el nombre de la compañia: ";
        cin>>nombre_compania[i];
        cout<<"Cual es el nombre del trabajador: ";
        cin>>nombre_trabajador[i];
        while (bandera=="T")
        {
            system("cls");
            cout<<"Dijite el numero de la opcion que busca\n1) Ingresar Producto\n2) Factura\n3) Total de IVA\n4) Salir\nEleccion: ";
            cin>>opcion;
            switch (opcion)
            {
            case 1:
                system("cls");
                llenadofuncion();
                break;
            case 2:
                system("cls");
                facturarfuncion(nombre_compania,nombre_trabajador,i);
                getch();
                break;
            case 3:
                system("cls");
                total_facturas[i] = totalfuncion(nombre_compania,nombre_trabajador,subtotal_facturas,i);
                getch();
                break;
            case 4:
                bandera="F";
                break;
            default:
                break;
            }
            subtotal_facturas[i] = subtotalfuncion();
        }
    }
    suma_total_facturas = sumafacturas(n, total_facturas, nombre_compania, nombre_trabajador);
    cout<<"\nLa suma total de todas las facturas: "<<suma_total_facturas;
    cout<<"\n\nFin Del Programa";
    getch();
}