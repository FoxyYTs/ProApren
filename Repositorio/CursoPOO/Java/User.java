package Repositorio.CursoPOO.Java;

public class User extends Account{//User Hereda de Account  

    public User(String name, String document, String email, String password) {
        super(name, document, email, password);
    }
    void printDataUser(){
        System.out.println("Documento: " + document + "\nNombre: " + name + "\nEmail: " + email + "\nContraseña: " + password);
    }
}
