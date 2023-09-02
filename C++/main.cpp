#include <iostream>
#include <vector>
using namespace std;

vector<string> llenar(){
    vector<string>nombre;
    string a;
    for (int i = 0; i < 3; i++){
        cout<<"Numero: ";
        cin>>a;
        nombre.push_back(a);
    }
    cout<<nombre.size();
    return nombre;
}
void imprimir(const vector<string>& nombre){
    for (int i = 0; i < nombre.size(); i++){
        cout<<i+1 << "#: "<<nombre[i]<<"\n";
    }
}

main(){
    vector<string>nombre;
    nombre = llenar();
    cout<<nombre.size();
    cout<<"\n===================\n";
    imprimir(nombre);
    
}

/*#include <iostream>
#include <vector>
using namespace std;

vector<double> carga_vector_v2(void);
void muestra_vector(const vector<double>&);

int main (){
  vector<double> v;
  v=carga_vector_v2();
  muestra_vector(v);
}

void muestra_vector(const vector<double>& v){
  for (size_t i = 0; i < v.size(); ++i)
        cout << v[i] << endl;
}

vector<double> carga_vector_v2(){
  int num_elementos;
  cout << "Introduce número de elementos: ";
  cin >> num_elementos;

  vector<double> v;
  v.reserve(num_elementos); // Creamos al menos num_elementos de capacidad

  for (int i = 0; i < num_elementos; ++i){
    double valor;
    cout << "\nIntroduce elemento " << i+1 << ": ";
    cin >> valor;
    v.push_back(valor);
  }
  return v;
}*/