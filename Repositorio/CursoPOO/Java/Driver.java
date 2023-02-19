package Repositorio.CursoPOO.Java;

public class Driver extends Account{

    public Driver(String name, String document, String email, String password) {
        super(name, document, email, password);
    }
    void printDataUser(){
        System.out.println("Documento: " + document + "\nNombre: " + name + "\nEmail: " + email + "\nContraseña: " + password);
    }
}
