#include <iostream>
using namespace std;

main(){
    const int x = 6;
    int lista[x] = {6,3,8,4,5,2};
    int aux;

    cout<<"lista = [";
    for (int i = 0; i < x; i++){
        cout<<lista[i]<<", ";
    }
    cout<<"]";
    for (int i = x-1; i > 0; i--){
        for (int j = 0; j < i; j++){
            if (lista[j]>lista[j+1]){
                aux = lista[j];
                lista[j] = lista[j+1];
                lista[j+1] = aux;
            }
        }
    }
    cout<<"\nlista = [";
    for (int i = 0; i < x; i++){
        cout<<lista[i]<<", ";
    }
    cout<<"] ordenada";


}
