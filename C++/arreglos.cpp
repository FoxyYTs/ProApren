#include <iostream>
using namespace std;

main(){
    int x,numero,j;
    int f,h,k,i;
    bool bsec = false ,bbin = false; 
    cout<<"Cuantos numeros pondras: ";
    cin>>x;

    int lista[x];
    for (int i = 0; i < x; i++){
        cout<<"Ingresa un numero: ";
        cin>>lista[i];
    }

    cout<<"Lista = [";
    for (int i = 0; i < x; i++){
        cout<<lista[i]<<", ";
    }
    cout<<"]\nIngresa un numero a buscar: ";
    cin>>numero;

    for (j = 0; j < x; j++){
        if (lista[j]==numero){
            bsec = lista[j]==numero;
            break;
        }
        
    }
    if (bsec){
        cout<<"\nEl numero: "<<numero<<" se encuentra en la pocicion "<< j;
    }else{
        cout<<"\nEl numero que busca no se encuentra en esta lista";
    }
    cout<<"\nEsa fue la Busqueda Secuencial\n";


    i = 0;
    j = x-1;
    do{
        k = (i+j)/2;
        if (lista[k]<numero){
            i = k+1;
        }else if(lista[k]>numero){
            j = k-1;
        }else{
            bbin = true;
            break;
        }
    }while(i <= j);

    if (bbin){
        cout<<"\nEl numero: "<<numero<<" se encuentra en la pocicion "<< k;
    }else{
        cout<<"\nEl numero que busca no se encuentra en esta lista";
    }
    cout<<"\nEsa fue la Busqueda Binaria\n";
}