#include <iostream>
using namespace std;
string name[50];
float nota[50];
int cant;

string llenado(int x){
    cout<<"Nombre: ";
    cin>>name[x];
    cout<<"Nota: ";
    cin>>nota[x];      
}

int nombres(int h){
    cout<<h+1<<" Estudiante: "<<name[h];
}
float nom_not(int h){
    cout<<"\nEstudiante: "<<name[h]<<"\nNota: "<<nota[h];
}
string busca(string nombre){
    int x;
    bool bandera = false;
    for (x = 0;bandera==false && x < cant; x++){
        if (name[x]==nombre){
            bandera=true;
            x--;
        }	
	} 
    if(bandera){
        cout<<"\nEl Estudiante "<<nombre<<" En la posicion "<<++x<<" tiene la nota: "<<nota[x];
    }else{
        cout<<"\nEl Estudiante: "<<nombre<<" No se encuentra en clase";
    }
}
float mod(float cambio,string nombre){
    int x;
    bool bandera = false;
    for (x = 0;bandera==false && x < cant; x++){
        if (name[x]==nombre){
            bandera=true;
            x--;
        }	
	} 
    if(bandera){
        cout<<"\nLa Nota del Estudiante: "<<nombre<<" Era: "<<nota[x]<<" y sera cambiada por: "<<cambio;
        nota[x]=cambio;
    }else{
        cout<<"\nEl Estudiante: "<<nombre<<" No se encuentra en clase";
    }
}

main(){
    float prom=0,change;
    string nombre;
    system("cls");
    cout<<"Cuantos estudiantes ingresaras: ";
    cin>>cant;
    for (int i = 0; i < cant; i++){
        cout<<"\n==========================";
        llenado(i);
    }
    
    system("cls");
    for (int i = 0; i < cant; i++){
        cout<<"\n==========================";
        nombres(i);
        nom_not(i);
        prom += nota[i];
    }
    cout<<"\nPromedio de todos los estudiantes: "<<prom/cant;
    cout<<"\n==========================";
    cout<<"\nIngresa el nombre: ";
    cin>>nombre;
    busca(nombre);
    cout<<"\n==========================";
    cout<<"\nIngresa el nombre: ";
    cin>>nombre;
    cout<<"\nIngresa la nota: ";
    cin>>change;
    mod(change,nombre);
    prom=0;
	for (int i = 0; i < cant; i++){
        cout<<"\n==========================";
        nombres(i);
        nom_not(i);
        prom += nota[i];
    }
    cout<<"\nPromedio de todos los estudiantes: "<<prom/cant;
}