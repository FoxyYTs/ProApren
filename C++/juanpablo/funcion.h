#include <iostream>
using namespace std;

string producto[100];
int precio[100],cantidad[100],preciototal[100],subtotalG,n,i;
string empresa,nombre;

void llenar(string nomEmpre[],string nomEmple[],int j){
    i = j,empresa = nomEmpre[i],nombre = nomEmple[i];
    cout<<"cuantos elementos hay en la factura: ";
    cin>>n;
    for (int j = 0; j < n; j++){
        cout<<"Ingresa el "<<j+1<<" producto: ";
        cin>>producto[j];
        cout<<"Ingresa la cantidad: ";
        cin>>cantidad[j];
        cout<<"Ingresa el precio individual: ";
        cin>>precio[j];
    }
}

int totaldiscreto(){
    subtotalG = 0;
    for (int j = 0; j < n; j++){
        preciototal[j] = cantidad[j] * precio[j];
        subtotalG += preciototal[j];
    }
    int iva,descuento = subtotalG*0.05,cantidadtotal=0,subto = subtotalG-descuento,total ;
    for (int j = 0; j < n; j++){
        cantidadtotal += cantidad[j];
    }
    if(cantidadtotal > 30){
        iva = subto*0.19,total = subto+iva;
    }else{
        iva = subtotalG*0.19, total = subtotalG+iva;
    }
    return total;
}

void facturar(){
    int subtotal = 0,cantidadtotal=0;
    cout<<"Empresa "<<empresa<<"\n";
    cout<<"Facturador "<<nombre<<"\n";
    cout<<"--------------------"<<"\n";
    for (int j = 0; j < n; j++){
        preciototal[j] = cantidad[j]*precio[j];
        cout<<j+1<<" Elemento "<<producto[j]<<" Cantidad "<<cantidad[j]<<" Precio individual "<<precio[j]<<" Precio total "<<preciototal[j]<<"\n";
        subtotal += preciototal[j];
        cantidadtotal += cantidad[j];
    }
    cout<<"--------------------\n";
    cout<<"Cantidad productos "<<cantidadtotal<<" Suma de todos los precios "<<subtotal;
}

void total(){
    int iva,descuento = subtotalG*0.05,cantidadtotal=0,subto = subtotalG-descuento,total ;
    cout<<"Empresa "<<empresa<<"\n";
    cout<<"Facturador "<<nombre<<"\n";
    cout<<"--------------------"<<"\n";
    for (int j = 0; j < n; j++){
        cout<<"Producto "<<producto[j]<<" Cantidad "<<cantidad[j]<<" Precio total "<<preciototal[j]<<"\n";
        cantidadtotal += cantidad[j];
    }
    cout<<"--------------------\n";
    if(cantidadtotal > 30){
        iva = subto*0.19,total = subto+iva;
        cout<<"Gracias a que a comprado mas de 30 productos recibe un descuento del 5%\n";
        cout<<"Cantidad productos "<<cantidadtotal;
        cout<<"\nsubtotal "<<subtotalG;
        cout<<"\nDescuento "<< descuento;
        cout<<"\nSubtotal con descuento "<<subto;
        cout<<"\nIVA "<< iva;
        cout<<"\nTotal "<<total;
    }else{
        iva = subtotalG*0.19, total = subtotalG+iva;
        cout<<"No cumple los requisitos para recibir descuento\n";
        cout<<"Cantidad productos "<<cantidadtotal;
        cout<<"\nsubtotal "<<subtotalG;
        cout<<"\nDescuento "<< 0;
        cout<<"\nSubtotal con descuento "<<subtotalG;
        cout<<"\nIVA "<< iva;
        cout<<"\nTotal "<<total;
    }
}
int sumfacturas(string empresa[],string nombre[],int totales[],int cantidad_facturas){
    int suma_totales = 0;
    for (int f = 0; f < cantidad_facturas; f++)
    {
        cout<<"\n#"<<f+1;
        cout<<"\nEmpresa: "<<empresa[f]<<" Facturador: "<<nombre[f]<<" Total: "<<totales[f];
        suma_totales += totales[f];
    }
    return suma_totales;
}