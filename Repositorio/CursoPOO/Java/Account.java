package Repositorio.CursoPOO.Java;

public class Account {
    int id;
    String nombre;
    String documento;
    String correo;
    String contraseña;

    public Account(int id, String nombre, String documento, String correo, String contraseña){
        this.id = id;
        this.nombre = nombre;
        this.documento = documento;
        this.correo = correo;
        this.contraseña = contraseña;
    }

}
