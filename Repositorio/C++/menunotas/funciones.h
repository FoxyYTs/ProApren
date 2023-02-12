#include <iostream>
using namespace std;

/*vector<string> names;
    vector<float> notas;*/

void llenar(vector<string> names,vector<float> notas){
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
/*float imprimir(){
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
}*/