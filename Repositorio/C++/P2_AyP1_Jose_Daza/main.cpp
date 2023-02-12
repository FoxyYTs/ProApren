#include <iostream>
#include <conio.h>
#include <vector>
#include "funciones.h"
using namespace std;
/*Crear un programa que realice las liquidaciones de n empleados, así: prima, vacaciones,
cesantías, intereses a las cesantías, teniendo en cuenta:
Liquidar prestaciones sociales en Colombia:
- Prima de servicios: (Salario mensual * Días trabajados en el semestre) / 360

- Cesantías: (Salario mensual * Días trabajados) / 360
- Intereses sobre cesantías: (Cesantías * Días trabajados * 0,12) / 360
- Vacaciones:(Salario diario * 15 días hábiles o lo días que vaya a tomar el empleado
(+ sábados, domingos y festivos en las fechas solicitadas). Debe imprimir todo.

MENÚ:
1. Prima
2. Vacaciones
3. Cesantías
4. Intereses sobre Cesantías
5. Totales pagados
6. Salir*/

main(){
    cout<<"+++++++++++Inicio+++++++++++";
    cout<<"\nDale 'ENTER' para continuar";
    getch();
    vector<string> nombre;
    vector<int> salario,diasT,primaV, vacacionesV, cesantiasV,InteresesV,totalpV;
    bool con_us = true;
    int op,dayw,salary;
    string name, con;
    for (int i = 0;con_us; i++){
        bool con_sw = true;
        system("cls");
        cout<<"Bienvenido al gestor de liquidacion\nNombre: ";
        cin>>name;
        nombre.push_back(name);
        cout<<"Salario: ";
        cin>>salary;
        salario.push_back(salary);
        cout<<"Dias Trabajados: ";
        cin>>dayw;
        diasT.push_back(dayw);
        primaV.push_back(primainco(nombre,salario,diasT,i));
        vacacionesV.push_back(vacainco(nombre,salario,diasT,i));
        cesantiasV.push_back(cesainco(nombre,salario,diasT,i));
        InteresesV.push_back(interinco(nombre,cesantiasV,diasT,i));
        totalpV.push_back(totalinco(nombre,salario,primaV,vacacionesV,cesantiasV,InteresesV,diasT,i));
        while (con_sw){
            system("cls");
            cout<<"Elige la opcion que quieras revisar\n1) Prima\n2) Vacaciones\n3) Cesantias\n4) Intereses sobre Cesantias\n5) Totales Pagados \n6) Siguiente empleado o Salir\nEleccion: ";
            cin>>op;
            switch (op){
            case 1:
                system("cls");
                prima(nombre,salario,diasT,i);
                cout<<"\nDale 'ENTER' para continuar";
                getch();
                break;
            case 2:
                system("cls");
                vacaciones(nombre,salario,diasT,i);
                cout<<"\nDale 'ENTER' para continuar";
                getch();
                break;
            case 3:
                system("cls");
                cesantias(nombre,salario,diasT,i);
                cout<<"\nDale 'ENTER' para continuar";
                getch();
                break;
            case 4:
                system("cls");
                intecesa(nombre,cesantiasV,diasT,i);
                cout<<"\nDale 'ENTER' para continuar";
                getch();
                break;
            case 5:
                system("cls");
                totalp(nombre,salario,primaV,vacacionesV,cesantiasV,InteresesV,diasT,i);
                cout<<"\nDale 'ENTER' para continuar";
                getch();
                break;
            case 6:
                system("cls");
                cout<<"Terminando la liquidacion de :"<<nombre[i];
                con_sw = false;
                cout<<"\nDale 'ENTER' para continuar";
                getch();
                break;
            default:
                break;
            }
        }
        cout<<"\nQuieres ingresar mas trabajadores [y/n]: ";
        cin>>con;
        if(con == "n"){
            con_us = false;
        }
    }
    system("cls");
    imprimir(nombre,salario,primaV,vacacionesV,cesantiasV,InteresesV,diasT,totalpV);
    cout<<"\n+++++++++++FIN+++++++++++";
    cout<<"\nDale 'ENTER' para continuar";
    getch();
}