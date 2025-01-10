#include<iostream>
using namespace std;
int main()
{
    cout<<"LENAR MATRIZ"<<endl;
    cout<<endl;
    int i,j,filas,columnas;
    int matriz [5][5];
    cout<<"Ingrese el numero de filas: "<<endl;
    cin>>filas;
    cout<<"Ingrese el numero de columnas: "<<endl;
    cin>>columnas;
    for (i=0; i<filas; i++){
        for (j=0; j<columnas;j++){
            cout<<"Ingrese un numero: "<<endl;
            cin>>matriz[i][j];
        }
     }
    for (i=0;i<filas;i++){
    	cout<<"[ ";
        for (j=0;j<columnas;j++){
            cout<<matriz[i][j]<<" ";
        }
        cout<<"]"<<endl;
	}    
	// PRIMERA FORMA DE "ENCONTRAR, IMPRIMIR, VER" LA DIAGONAL PRINCIPAL
	cout<<"Diagonal principal";
	for (i=0; i<filas; i++){
		cout<<"\n"<<matriz[i][i];
	}
	cout<<endl;
	//SEGUNDA FORMA DE HACERLO
	cout<<"Diagonal principal #2";
	for (i=0; i<filas; i++){
        for (j=0; j<columnas;j++){
            if(i==j){
            	cout<<"\n"<<matriz[i][j];
            
			}
        }
     }
    cout<<endl;
    //DIAGONAL SECUNDARIA 
    cout<<"La diagonal secundaria es: ";
    for (i=0; i<filas; i++){
        for (j=0; j<columnas;j++){
            if(i!=j){
            	cout<<"\n"<<matriz[i][j]; 
            	
			}
        }
    }
}