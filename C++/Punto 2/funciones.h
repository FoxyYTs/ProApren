#include <iostream>
using namespace std;

string servicio_producto[100];
int cantidad[100],n;
float precio[100],precio_total[100]; 

void llenadofuncion()
{
    cout<<"cuantos elementos ingresaras\n";
    cin>>n;
    for (int j = 0; j < n; j++)
    {
        cout<<"Ingresa el Producto o servicio"<<" #"<<j+1<<": ";
        cin>>servicio_producto[j];
        cout<<"Ingresa el precio del elemento: ";
        cin>>precio[j];
        cout<<"Ingresa la cantidad de elementos: ";
        cin>>cantidad[j];
    }
}

void facturarfuncion(string compania[],string nombre[],int i)
{
    int subtotal = 0,cantit=0;
    cout<<"Compañia "<<compania[i]<<"\n";
    cout<<"Facturador "<<nombre[i]<<"\n";
    cout<<"====================\n";
    for (int j = 0; j < n; j++)
    {
        precio_total[j] = cantidad[j]*precio[j];
        cout<<"Elemento: "<<servicio_producto[j]<<" Cantidad: "<<cantidad[j]<<" Precio individual "<<precio[j]<<" Precio total "<<precio_total[j]<<"\n";
        subtotal = subtotal + precio_total[j];
        cantit = cantit + cantidad[j];
    }
    cout<<"====================\n";
    cout<<"Cantidad elementos "<<cantit<<" Suma de todos los precios "<<subtotal;
}

int totalfuncion(string compania[],string nombre[],int subtotal[],int i)
{
    int iva,descuento = subtotal[i]*0.15,cantit=0,subtotal_decuento = subtotal[i]-descuento,total ;
    cout<<"Compañia "<<compania[i]<<"\n";
    cout<<"Facturador "<<nombre[i]<<"\n";
    cout<<"====================\n";
    for (int j = 0; j < n; j++)
    {
        cout<<"Producto "<<servicio_producto[j]<<" Cantidad "<<cantidad[j]<<" Precio total "<<precio_total[j]<<"\n";
        cantit = cantit + cantidad[j];
    }
    cout<<"====================\n";
    if(cantit > 10)
    {
        iva = subtotal_decuento*0.19,total = subtotal_decuento+iva;
        cout<<"tienes mas de 10 elementos por lo que se le aplicara un descuento del 15%\n";
        cout<<"Cantidad Elementos "<<cantit<<"\nsubtotal "<<subtotal[i]<<"\nDescuento "<< descuento <<"\nSubtotal con descuento "<<subtotal_decuento<<"\nIVA "<< iva <<"\nTotal "<<total;
    }
    else
    {

        iva = subtotal[i]*0.19, total = subtotal[i]+iva;
        cout<<"No se a aplicado ningun descuento\n";
        cout<<"Cantidad Elementos "<<cantit<<"\nsubtotal "<<subtotal[i]<<"\nDescuento "<< 0 <<"\nSubtotal con descuento "<<subtotal[i]<<"\nIVA "<< iva <<"\nTotal "<<total;
    }
    return total;
}
int sumafacturas(int cantidad_facturas,int totales[],string compania[],string nombre[]){
    int suma_totales = 0;
    for (int i = 0; i < cantidad_facturas; i++)
    {
        cout<<"\n#"<<i+1<<"\nCompañia: "<<compania[i]<<"Facturador: "<<nombre[i]<<"Total: "<<totales[i];
        suma_totales = suma_totales + totales[i];
    }
    return suma_totales;
}

float subtotalfuncion()
{
    int subtotal = 0;
    for (int j = 0; j < n; j++)
    {
        precio_total[j] = cantidad[j] * precio[j];
        subtotal = subtotal + precio_total[j];
    }
    return subtotal;
}