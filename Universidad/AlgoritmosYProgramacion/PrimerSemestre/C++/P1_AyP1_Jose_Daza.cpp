#include <iostream>
using namespace std;
main(){
    /*
    //Ejercicio 1
    int numero=0, suma=0, multiplicacion=0,limite=0;
    //numero = E, suma = S, multiplicacion = S, limite = E
    cout<<"\nInicio del Programa";
    cout<<"Bienvenido al ejercicio numero 1:Multiplicacion\nCuantos numeros quiere multiplicar: ";
    cin>>limite;
    for (int i = 0; i < limite; i++)
    {
        cout<<"\nIngrese Un numero para multiplicar por 5: ";
        cin>>numero;
        multiplicacion = numero * 5;//Proceso
        suma += multiplicacion;//Proceso 
        cout<<"\nLa Multiplicacion de su numero es: "<<multiplicacion;
    }    
    cout<<"\nLa suma de todas las multiplicaciones es: "<<suma<<" La multiplicacion se a realizado por el numero 5\nFin Del Programa";
    */
    //Ejercicio 2
    int total=0, costcre = 50000, costo=0,creditos=0,descuento=0;
    //total = S, costcre = P, costo = S, creditos = E, descuento = P
    string repetir="Seguir", materia, name,comfama="no";
    //repetir = E, materia = E,name = E, comfama = E
    cout<<"\nInicio del Programa";
    cout<<"Bienvenido al Ejercicio de Matricula Universitaria";
    for (int i = 0; repetir != "Salir"; i++){
        cout<<"Bienvenido al programa de matricula de materias\nnecesita matricular 5 materias para que sea efectivo, cada credito equivale a 50000";
        cout<<"\nCual es su nombre: ";
        cin>>name;
        for (int j = 1; j <= 5; j++){
        	int costopormateria=0;
            cout<<"\n======================================================";
            cout<<"\n\nIngrese el codigo de la materia: ";
            cin>>materia;
            cout<<"\nIngrese el numero de creditos: ";
            cin>>creditos;
            costopormateria = creditos * costcre;
            costo+=costopormateria;
            cout<<"\nAsignatura: "<<materia;
            cout<<"\nCreditos: "<< creditos;
            cout<<"\nValor Asignatura: "<<costopormateria;
            
            cout<<"\nLleva "<< j <<" Materias inscritas";
        }
        cout<<"\n======================================================";
        cout<<"\nUsted es beneficiario de comfama? si/no:";
        cin>>comfama;
        if(comfama == "si"){
        	cout<<"Felicidades a aplicado a un desuento del 10%";
        	descuento = costo*0.10;
		}
		total = costo - descuento;
		cout<<"\n======================================================";
        cout<<"\nEstudiante: "<<name;
        cout<<"\nValor Credito: 50000";
        cout<<"\nSubTotal: "<<costo;
        cout<<"\nDescuento: "<<descuento;
        cout<<"\nTotal: "<<total;
        cout<<"\n======================================================";
        cout<<"\nCuando ya todos los alumnos terminen de inscribirce dijite 'Salir' de lo contrario ponga otra cosa:";
        cin>>repetir;
        
    }
    cout<<"\nFin del Programa";
}