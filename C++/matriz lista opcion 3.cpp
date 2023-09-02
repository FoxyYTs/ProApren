#include<iostream>

using namespace std;

float x=0;
const int fila = 10, colu = 10;
int matriz[fila][colu], f=0,h=0,w;

int llenado(int x){
    matriz[f][h]=x;
    if (h>=fila){
        h=0;
        f++;
    }
    h++;
    return 0;         
}
void imprimir(){
    for(int i = 0;i<fila;i++){
        float y=0;
        cout<<"\n";
        cout<<"[ ";
        for(int j = 0;j<colu;j++){
            cout<<matriz[i][j]<<"\t ";
            x+=matriz[i][j],y+=matriz[i][j];
        }
        cout<<"] Suma: "<<y<<" Promedio: "<<y/fila;
    }
    cout<<"\nSuma: "<<x<<"\nPromedio: "<<x/(fila*colu);
}
void diagonal_p(){
    cout<<"Diagonal principal";
	for (int i=0; i<fila; i++){
		cout<<"\n"<<matriz[i][i];
	}
}
void diagonal_s(){
    cout<<"\nDiagonal secundaria";
	for(int i = 0;i<fila;i++){
        for(int j = 0;j<colu;j++){
            if(((i+1)+(j+1))==fila+1){
                cout<<"\n"<<matriz[i][j];
            }
        }
    }
}
void juntas(){
    cout<<"\nJuntas\n";
    for(int i = 0;i<fila;i++){
        for(int j = 0;j<colu;j++){
            if(((i+1)+(j+1))==fila+1||i==j){
                cout<<matriz[i][j]<<"\t";
            }else{
                cout<<"-\t";
            }
        }
        cout<<"\n";
    }
}
int main(){
    int ing;
    cout<<"++++Llenado de matriz por funcion Opcion 3++++\n";
    for(int i = 0; i<(fila*colu);i++){
        cout<<"Ingresa un Numero: ";
        ing = i+1;
        llenado(ing);
    }
    
    imprimir();
    
    cout<<"\n========";
    
    diagonal_p();

    diagonal_s();

    juntas();
    //invertido();
    cout<<"\n++++Fin++++";
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