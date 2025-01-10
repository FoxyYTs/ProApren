#include <iostream>
#include "conio.h"
#include<string>
using namespace std;

int main()
{
    int fila, columna, suma=0,x=1,y=0;
    cout << "ingrese numero de filas: ";
    cin >> fila;
    cout << "ingrese numero de columnas: ";
    cin >> columna;
    int numeros[10][10];

    for (int i = 0; i < fila; i++)
    {
        
        for (int j = 0; j < columna ; j++)
        {
            numeros[i][j] = x++;
            if(numeros[i][j]%5==0){
                y++;
            }
            suma=suma+numeros[i][j];
        }
        
    }
    
  
    cout<<"____"<<endl;
    for (int i = 0; i < fila; i++)
    {
        cout<<"[  ";
        
        for (int j = 0; j < columna; j++)
        {
            cout << numeros[i][j]<<"  ";
        }
        cout<<"]";
        cout << endl;
    }
    cout<<"____"<<endl;
    
    cout<<"____"<<endl;

    for (int i = 0; i < y/2; i++){
        cout<<"[  ";
        for (int j = 0; j < y/2; j++){
            if(numeros[i][j]%5==0){
                cout<<numeros[i][j]<<"  ";
            }
        }
        cout<<"]";
        cout << endl;
    }
    cout<<"____"<<endl;
    
    cout<<"la suma es: "<<suma;
    return 0;
}