
#include <iostream>
#include <conio.h>
#include<math.h>
#include <vector>

using namespace std;

/*int dayv,findes,vac;
    cout<<"Cuantos dias tomara de vacaciones: ";
    cin>> dayv;
    cout<<"Cuantos fines de semana o festivos se le suman: ";
    cin>> findes;
    vac = ((salary[i]/30)*dayv+findes);
    cout<<"Senor/a "<< name[i]<<" Su salario diario es de: "<<(salary[i]/30)<<" y esta pidiendo un total de: "<<(dayv+findes)<<" dias de vacaciones pagadas por los cuales recibira: "<<vac;
    return vac;*/

void prima(vector<string> name,vector<int> salary,vector<int> dayw, int i){
    int prima = (salary[i] * dayw[i])/360,prima1=(salary[i]*180)/360,prima2=(salary[i]*(dayw[i]-180))/360;
    if (dayw[i] > 180){
        cout<<"Empleado: "<< name[i]<<"\nsalario mensual es de: "<<salary[i]<<"\ndias trabajados son: "<<dayw[i]<<"\nPrima primer semestre: "<<prima1<<"\nPrima segundo semestre: "<<prima2;
    }else{
        cout<<"Empleado: "<< name[i]<<"\nsalario mensual es de: "<<salary[i]<<"\ndias trabajados son: "<<dayw[i]<<"\nPrima primer semestre: "<<prima;
    }
}
void vacaciones(vector<string> name,vector<int> salary,vector<int> dayw, int i){
    float vac = (salary[i]*dayw[i])/720;
    int vacf = ceil(vac);
    cout<<"Empleado: "<< name[i]<<"\nsalario mensual es de: "<<salary[i]<<"\ndias trabajados son: "<<dayw[i]<<"\npor lo cual en sus vacaciones recibe un total de: "<<vacf;
}
void cesantias(vector<string> name,vector<int> salary,vector<int> dayw, int i){
    int cesa = (salary[i]*dayw[i])/360;
    cout<<"Empleado: "<< name[i]<<"\nsalario mensual es de: "<<salary[i]<<"\ndias trabajados son: "<<dayw[i]<<"\npor lo cual sus Cesantias correspondientes son: "<<cesa;
}
void intecesa(vector<string> name,vector<int> cesantias,vector<int> dayw, int i){
    float inte = (cesantias[i]*dayw[i]*0.12)/360;
    int intef = ceil(inte);
    cout<<"Empleado: "<< name[i]<<"\nCesantias son: "<<cesantias[i]<<"\ndias trabajados son: "<<dayw[i]<<"\npor lo cual los intereses son de: "<<intef;
}
void totalp(vector<string> name,vector<int> salary,vector<int> prima,vector<int> vacaciones,vector<int> cesantias,vector<int> Intereses, vector<int> dayw, int i){
    int total = cesantias[i]+Intereses[i]+prima[i]+vacaciones[i],prima1=(salary[i]*180)/360,prima2=(salary[i]*(dayw[i]-180))/360;
    if(dayw[i] > 180){
        cout<<"Empleado: "<< name[i]<<"\na continuacion se mostrara la informacion de la liquidacion\n==========\nCesantias: "<<cesantias[i]<<"\nIntereses Sobre Cesantias: "<<Intereses[i]<<"\nPrima primer semestre: "<<prima1<<"\nPrima segundo semestre: "<<prima2<<"\nVacaciones: "<<vacaciones[i]<<"\nTOTAL: "<<total;
    }else{
        cout<<"Empleado: "<< name[i]<<"\na continuacion se mostrara la informacion de la liquidacion\n==========\nCesantias: "<<cesantias[i]<<"\nIntereses Sobre Cesantias: "<<Intereses[i]<<"\nPrima primer semestre: "<<prima[i]<<"\nVacaciones: "<<vacaciones[i]<<"\nTOTAL: "<<total;
    }
}
void imprimir(vector<string> name,vector<int> salary,vector<int> prima,vector<int> vacaciones,vector<int> cesantias,vector<int> Intereses, vector<int> dayw, vector<int> total){
    int prima1,prima2;
    if (name.size() != 0){
        for (int i = 0; i < name.size(); i++){
            prima1=(salary[i]*180)/360,prima2=(salary[i]*(dayw[i]-180))/360;
            cout<<"\n=========================="<<i+1<<" Trabajador: "<<name[i];
            if(dayw[i] > 180){
                cout<<"\nTrabajador: "<<name[i]<<"\nSalario: "<<salary[i]<<"\nCesantias: "<<cesantias[i]<<"\nIntereses Sobre Cesantias: "<<Intereses[i]<<"\nPrima primer semestre:: "<<prima1<<"\nPrima segundo semestre:: "<<prima2<<"\nVacaciones: "<<vacaciones[i]<<"\nTOTAL: "<<total[i];
            }else{
                cout<<"\nTrabajador: "<<name[i]<<"\nSalario: "<<salary[i]<<"\nCesantias: "<<cesantias[i]<<"\nIntereses Sobre Cesantias: "<<Intereses[i]<<"\nPrima: "<<prima[i]<<"\nVacaciones: "<<vacaciones[i]<<"\nTOTAL: "<<total[i];
            }
        }
    }else{
        cout<<"La lista esta Vacia";
    }
}
int primainco(vector<string> name,vector<int> salary,vector<int> dayw, int i){
    int prima = (salary[i] * dayw[i])/360;
    return prima;
}
float vacainco(vector<string> name,vector<int> salary,vector<int> dayw, int i){
    float vac = ((salary[i]*dayw[i])/720);
    int vacf = ceil(vac);
    return vac;
}
int cesainco(vector<string> name,vector<int> salary,vector<int> dayw, int i){
    int cesa = (salary[i]*dayw[i])/360;
    return cesa;
}
int interinco(vector<string> name,vector<int> cesantias,vector<int> dayw, int i){
    float inte = (cesantias[i]*dayw[i]*0.12)/360;
    int intef = ceil(inte);
    return intef;
}
int totalinco(vector<string> name,vector<int> salary,vector<int> prima,vector<int> vacaciones,vector<int> cesantias,vector<int> Intereses, vector<int> dayw, int i){
    int total = cesantias[i]+Intereses[i]+prima[i]+vacaciones[i];
    return total;
}
 