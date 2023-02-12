#include<iostream>

using namespace std;

float x=0;
const int fila = 3, colu = 3;
int matriz[fila][colu], f=0,h=0;

void llenado(){
    for(int i = 0;i<fila;i++){
        for(int j = 0;j<colu;j++){
            cout<<"Ingresa un Numero: ";
            cin>>matriz[i][j];
        }
    }        
}
void imprimir(){
    for(int i = 0;i<fila;i++){
        float y=0;
        cout<<"\n";
        cout<<"[ ";
        for(int j = 0;j<colu;j++){
            cout<<matriz[i][j]<<" ";
            x+=matriz[i][j];
            y+=matriz[i][j];
        }
        cout<<"] Suma: "<<y<<" Promedio: "<<y/fila;
    }
    cout<<"\nSuma: "<<x<<"\nPromedio: "<<x/(fila*colu);
}
void invertido(){
    for(int i = fila-1;i>=0;i--){
        cout<<"\n";
        cout<<"[ ";
        for(int j = colu-1;j>=0;j--){
            cout<<matriz[i][j]<<" ";
        }
        cout<<"]";
    }
}

int main(){
    cout<<"++++Llenado de matriz por funcion Opcion 1++++\n";
    llenado();

    imprimir();
    
    cout<<"\n========";
    
    invertido();
    cout<<"\n++++Fin++++";
}