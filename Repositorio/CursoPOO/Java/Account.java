package Repositorio.CursoPOO.Java;

public class Account {
    private int id;
    private String nombre;
    private String documento;
    private String correo;
    private String contraseña;

    public Account(String nombre, String documento, String correo, String contraseña){
        this.nombre = nombre;
        this.documento = documento;
        this.correo = correo;
        this.contraseña = contraseña;
    }

    public void setId(int id){
        this.id = id;

    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public void setDocumento(String documento){
        this.documento = documento;
    }

    public void setCorreo(String correo){
        this.correo = correo;
    }

    public void setContraseña(String contraseña){
        this.contraseña = contraseña;
    }

    public int getId(){
        return id;
    }

    public String getNombre(){
        return nombre;
    }

    public String getDocumento(){
        return documento;
    }

    public String getCorreo(){
        return correo;
    }

    public String getContraseña(){
        return contraseña;
    }

}
