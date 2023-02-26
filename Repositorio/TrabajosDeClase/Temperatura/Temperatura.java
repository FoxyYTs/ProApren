package Repositorio.TrabajosDeClase.Temperatura;

public class Temperatura {

    public double KaC(double k) {
        return k-273.13;
    }

    public double KaF(double k){
        return ((9*(k-273.15))/5)+32;
    }
    
    public double FaK(double f){
        return ((5*(f-32))/9);
    }

    public double FaC(double f){
        return ((5*(f-32))/9)+273.15;
    }

    public double CaK(double c){
        return c + 273.15;
    }
    
    public double CaF(double c){
        return ((9*c)/5)+32;
    }
}
