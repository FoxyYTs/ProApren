#include <iostream>
using namespace std;

main(){
    int victima,restante,i;
    cout<<"Ingrese la victima a dividir: ";
    cin>>victima;
    cout<<"Ingrese el Restante que dividira a la victima: ";
    cin>>restante;
    cout<<"\nDivicion "<<victima/restante;
    cout<<"\nModulo "<<victima%restante;
    for(i = 0;victima >= restante;i++){
        victima-=restante;
    }
    cout<<"\nDivicion por resta "<<i;
    cout<<"\nModulo por resta "<<victima;
}