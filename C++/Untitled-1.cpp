#include<iostream>

using namespace std;

int i, j, filas, columnas, matriz[10][10], suma=0;
//Función llenar la matriz
int llenar_matriz(int matriz[10][10],  int filas, int columnas){
	for(i=0; i<filas; i++){
		for(j=0;j<columnas;j++){
			cout<<"Ingrese el elemento: ["<<i<<"] ["<<j<<"]: ";
			cin>>matriz[i][j];
			suma=suma+matriz[i][j];
		}
		
	}
}
//Función Imprimir la matriz
int imprimir_mat(int matriz[10][10], int filas, int columnas){
	cout<<"Imprime la matriz"<<"\n";	
	for(int i=0; i<filas; i++){
		cout<<"[ ";
		for(int j=0;j<columnas;j++){
			cout<<matriz[i][j]<<" ";			
		}
		cout<<" ]";	
		cout<<"\n";
	}
}
main(){
    cout<<"Ingrese el numero de filas: ";
	cin>>filas;
	cout<<"Ingrese el numero de columnas: ";
	cin>>columnas;
	llenar_matriz(matriz, filas, columnas);
	system("cls");
	imprimir_mat(matriz, filas, columnas);
	
	cout<<"suma de los elementos de la matriz: "<<suma;
	return 0;
}