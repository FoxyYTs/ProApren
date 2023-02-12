#include <iostream>
using namespace std;

//Jose Andres Daza Gallego
//Jose Miguel Calderón Castaño
double Acua(double l){
    double acua;
    acua = l*l;
    return acua;
}

double Aret(double b,double h){
    double aret;
    aret = b*h;
    return aret;
}

double Acir(double r){
    double acir,pi = 3.1416;
    acir=pi*(r*r);
    return acir;
}

double Atria(double b, double h){
    double atria;
    atria = (b*h)/2;
    return atria;
}

main(){
    int opcion;
    double b,h,l,r;
    while(opcion != 5){
        cout<<"\n=========================";
        cout<<"\nCalculadora de areas\nIngrese el numero segun lo deseado\n1) Cuadrado\n2) Rectangulo \n3) Circulo \n4) Triangulo\n5) Salir del programa\nEleccion: ";
        cin>>opcion;
        switch (opcion){
            case 1:
                cout<<"Ingrese lado: ";
                cin>>l;
                cout<<"Area del Cuadrado: "<<Acua(l);
                break;
            case 2:
                cout<<"Ingrese Base: ";
                cin>>b;
                cout<<"Ingrese la Altura: ";
                cin>>h;
                cout<<"Area de Rectangulo: "<<Aret(b,h);
                break;
            case 3:
                cout<<"Ingrese el radio: ";
                cin>>r;
                cout<<"Area del Circulo: "<<Acir(r);
                break;
            case 4:
                cout<<"Ingrese Base: ";
                cin>>b;
                cout<<"Ingrese la Altura: ";
                cin>>h;
                cout<<"Area del Triangulo: "<<Atria(b,h);
                break;
            case 5:
                cout<<"Cerrando Programa";
                break;
            default:
                cout<<"\nEleccion incorrecta";
        }
    }
    cout<<"\nPrograma terminado";
}

