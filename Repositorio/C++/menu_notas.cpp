#include <iostream>
#include <conio.h>
#include <vector>
using namespace std;

vector<string> names;
vector<float> notas;

void llenar(){
    string conti="y",nom;
    float nota;
    cout<<"Ingresa el Nombre y la Nota del estudiante que quieras agregar";
    for (int i = 0;conti=="y"; i++){
            cout<<"\nNombre: ";
            cin>>nom;
            names.push_back(nom);
            cout<<"Nota: ";
            cin>>nota;
            notas.push_back(nota);
            cout<<"\nQuieres Agregar otro [y/n]: ";
            cin>>conti;
    }
}
float imprimir(){
    int prom = 0;
    if (names.size() != 0){
        for (int i = 0; i < names.size(); i++){
        cout<<"\n==========================";
        cout<<i+1<<" Estudiante: "<<names[i];
        cout<<"\nEstudiante: "<<names[i]<<"\nNota: "<<notas[i];
        prom += notas[i];
        }
        cout<<"\n==========================\nEl promedio de todo el grupo es: "<<prom/names.size();
    }else{
        cout<<"La lista esta Vacia";
    }
}
void busca(string nombre){
    int x;
    bool bandera = false;
    for (x = 0;bandera==false && x < names.size(); x++){
        if (names[x]==nombre){
            bandera=true;
            x--;
        }	
	} 
    if(bandera){
        cout<<"\nEl Estudiante "<<nombre<<" En la posicion "<<++x<<" tiene la nota: "<<notas[x];
    }else{
        cout<<"\nEl Estudiante: "<<nombre<<" No se encuentra en clase";
    }
}
void mod(float cambio,string nombre){
    int x;
    bool bandera = false;
    for (x = 0;bandera==false && x < names.size(); x++){
        if (names[x]==nombre){
            bandera=true;
            x--;
        }	
	} 
    if(bandera){
        cout<<"\nLa Nota del Estudiante: "<<nombre<<" Era: "<<notas[x]<<" y sera cambiada por: "<<cambio;
        notas[x]=cambio;
    }else{
        cout<<"\nEl Estudiante: "<<nombre<<" No se encuentra en clase";
    }
}
void eliminar(string nombre){
    int x;
    string elec;
    bool bandera = false;
    for (x = 0;bandera==false && x < names.size(); x++){
        if (names[x]==nombre){
            bandera=true;
            x--;
        }	
	} 
    if(bandera){
        cout<<"Seguro que quieres eliminar a "<<nombre<<" De la lista [y/n]: ";
        cin>>elec;
        if (elec == "y"){
            names.erase(names.begin()+x);
            notas.erase(notas.begin()+x);
        }
        
    }else{
        cout<<"\nEl Estudiante: "<<nombre<<" No se encuentra en clase";
    }
}

main(){
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
            llenar();
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
