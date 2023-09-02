#include <iostream>
using namespace std;

string producto[100];
int precio[100],cantidad[100],preciot[100];//Listas declaradas de forma global
int n;//cantidad de productos para limitar las listas



void llenado(){//funcion que guarda todos los productos en las listas globales
    cout<<"cuantos productos va a ingresar"<<endl;
    cin>>n;
    for (int j = 0; j < n; j++){
        cout<<"Ingresa el producto"<<" #"<<j+1<<endl;
        cin>>producto[j];
        cout<<"Ingresa la cantidad"<<endl;
        cin>>cantidad[j];
        cout<<"Ingresa el precio individual"<<endl;
        cin>>precio[j];
    }
}

int subtotalf(){//funcion que se ejecuta en segundo plano osea que no da ninguna señal de que se ejecuto y calcula la suma de todos los precios de los productos para que no sea olbigatorio primero entrar a la funcion factura() antes de entrar a la funcion total()
    int subtotal = 0;
    for (int j = 0; j < n; j++){
        preciot[j] = cantidad[j] * precio[j];
        subtotal = subtotal + preciot[j];
    }
    return subtotal;
}
int totalf(int subtotal[],int i){//funcion que se ejecuta en segundo plano osea que no da ninguna señal de que se ejecuto y calcula la suma de todos los precios de los productos para que no sea olbigatorio primero entrar a la funcion factura() antes de entrar a la funcion total()
    int iva,descuento = subtotal[i]*0.10,cantit=0,subto = subtotal[i]-descuento,total ;
    for (int j = 0; j < n; j++){
        cantit = cantit + cantidad[j];
    }
    if(cantit > 20){//condicional para aplicar el descuento segun la cantidad total de productos que esta comprando
        iva = subto*0.19,total = subto+iva;
    }else{
        iva = subtotal[i]*0.19, total = subtotal[i]+iva;
    }
    return total;
}

void facturar(string empresa[],string nombre[],int i){//funcion para ver todos los productos con sus precios individuales, precios totales y la suma de estos
    int subtotal = 0,cantit=0;
    cout<<"Empresa "<<empresa[i]<<endl;
    cout<<"Facturador "<<nombre[i]<<endl;
    cout<<"===================="<<endl;
    for (int j = 0; j < n; j++){
        preciot[j] = cantidad[j]*precio[j];
        cout<<"Producto "<<producto[j]<<" Cantidad "<<cantidad[j]<<" Precio individual "<<precio[j]<<" Precio total "<<preciot[j]<<endl;
        subtotal = subtotal + preciot[j];
        cantit = cantit + cantidad[j];
    }
    cout<<"===================="<<endl;
    cout<<"Cantidad productos "<<cantit<<" Suma de todos los precios "<<subtotal;
}

void total(string empresa[],string nombre[],int subtotal[],int i){//funcion que muestra y calcula el iva, el decuento y el total
    int iva,descuento = subtotal[i]*0.10,cantit=0,subto = subtotal[i]-descuento,total ;
    cout<<"Empresa "<<empresa[i]<<endl;
    cout<<"Facturador "<<nombre[i]<<endl;
    cout<<"===================="<<endl;
    for (int j = 0; j < n; j++){
        cout<<"Producto "<<producto[j]<<" Cantidad "<<cantidad[j]<<" Precio total "<<preciot[j]<<endl;
        cantit = cantit + cantidad[j];
    }
    cout<<"===================="<<endl;
    if(cantit > 20){//condicional para aplicar el descuento segun la cantidad total de productos que esta comprando
        iva = subto*0.19,total = subto+iva;
        cout<<"Gracias a que a comprado mas de 20 productos recibe un descuento del 10%"<<endl;
        cout<<"Cantidad productos "<<cantit<<endl<<" subtotal "<<subtotal[i]<<endl<<" Descuento "<< descuento <<endl<<" Subtotal con descuento "<<subto<<endl<<" IVA "<< iva <<endl<<" Total "<<total;
    }else{
        iva = subtotal[i]*0.19, total = subtotal[i]+iva;
        cout<<"No cumple los requisitos para recibir descuento"<<endl;
        cout<<"Cantidad productos "<<cantit<<endl<<" subtotal "<<subtotal[i]<<endl<<" Descuento "<< 0 <<endl<<" Subtotal con descuento "<<subtotal[i]<<endl<<" IVA "<< iva <<endl<<" Total "<<total;
    }
}