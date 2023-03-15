package Repositorio.ProyectoSegundoSemestre;

import java.util.ArrayList;

public class Grupo {
    private String nombre;
    private ArrayList<Contacto> contactos;

    public Grupo(String nombre){
        this.nombre = nombre;
        contactos = new ArrayList<Contacto>();
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void agregarContacto(Contacto contacto) {
        contactos.add(contacto);
    }
    
    public void eliminarContacto(Contacto contacto) {
        contactos.remove(contacto);
    }

    public void mostrarContacto(){
        for (Contacto i : contactos) {
            System.out.println(i.toString());
        }
    }
}
