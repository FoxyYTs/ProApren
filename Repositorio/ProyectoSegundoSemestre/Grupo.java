package Repositorio.ProyectoSegundoSemestre;

public class Grupo extends Agenda{
    private String nombre;
    private Contacto head;
    public Grupo next;

    public Grupo(String nombre){
        this.nombre = nombre;
        this.head = null;
        this.next = null;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public void insertarContactoGrupo(String nombre, String apellido, String correo, String telefono) {
        Contacto nuevo = new Contacto(nombre, apellido, correo, telefono);
        if (head == null) {
            head = nuevo;
        } else {
            Contacto pointer = head;
            while (pointer.next != null) {
                pointer = pointer.next;
            }
            pointer.next = nuevo;
        }
    }

    public void eliminarContactoGrupo(String nombre) {
        if (head == null) {
            return;
        }
        if (head.getNombre() == nombre) {
            head = head.next;
            return;
        }
        Contacto pointer = head;
        while (pointer.next.getNombre() != nombre && pointer.next != null) {
            pointer = pointer.next;
        }
        if (pointer.next != null) {
            pointer.next = pointer.next.next;
        }
    }

    public void mostrarContactoGrupo() {
        Contacto pointer = head;
        while (pointer != null) {
            configuracion.gruposMostrarContactos(pointer.getNombre(), pointer.getApellido(), pointer.getTelefono(), pointer.getCorreo());
            pointer = pointer.next;
        }
        System.out.println();
    }

}
