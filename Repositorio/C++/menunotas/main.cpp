#include <iostream>
#include <conio.h>
#include <vector>
#include "funciones.h"

using namespace std;

main(){
    vector<string> names;
    vector<float> notas;
    bool conti = true;
    int opt;
    string nom;
    float change;
    while(conti){
        system("cls");
        system("color 6");
        cout<<"Bienvenido al Gestor de notas de estudiantes\n\nSeleccion la Opcion que desea\n1) Llenar Lista\n2) Imprimir Lista\n3) Buscar\n4) Editar\n5) Eliminar\n0) Cerrar\nEleccion: ";
        cin>>opt;
        switch (opt){
        case 1:
            system("cls");
            system("color 1");
            cout<<"Bienvenido al sistema de llenado\n";
            llenar(names,notas);
            break;
        case 2:
            system("cls");
            system("color 2");
            imprimir();
            cout<<"\nDale 'ENTER' para continuar";
            getch();
            break;
        case 3:
            system("cls");
            system("color 3");
            cout<<"Bienvenido al sistema de busqueda\n";
            cout<<"Que estudiante quieres buscar: ";
            cin>>nom;
            busca(nom);
            cout<<"\nDale 'ENTER' para continuar";
            getch();
            break;
        case 4:
            system("cls");
            system("color 4");
            cout<<"Bienvenido al sistema de modificacion\n";
            cout<<"\nIngresa el nombre: ";
            cin>>nom;
            cout<<"\nIngresa la nota: ";
            cin>>change;
            mod(change,nom);
            cout<<"\nDale 'ENTER' para continuar";
            getch();
            break;
        case 5:
            system("cls");
            system("color 5");
            cout<<"Bienvenido al sistema de eliminacion\n";
            cout<<"Que estudiante quieres eliminar: ";
            cin>>nom;
            eliminar(nom);
            cout<<"\nDale 'ENTER' para continuar";
            getch();
            break;
        case 0:
            system("cls");
            cout<<"Cerrando el Programa";
            conti = false;
            cout<<"\nDale 'ENTER' para continuar";
            getch();
            break;
        
        default:
            cout<<"Opcion no valida";
            getch();
        }
    }
}