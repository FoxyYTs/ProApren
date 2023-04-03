package Repositorio.ProyectoSegundoSemestre;

public class Grupo {
    private String nombre;
    private Contacto head;
    private Contacto pointer;
    public Grupo next;

    public Grupo(String nombre){
        this.nombre = nombre;
        this.head = null;
        this.pointer = head;
        this.next = null;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public void insertarContacto(String nombre, String apellido, String correo, String telefono) {
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

    public void eliminarContacto(String nombre) {
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

    public void mostrarContacto() {
        Contacto pointer = head;
        while (pointer != null) {
            configuracion.gruposMostrarContactos(pointer.getNombre(), pointer.getApellido(), pointer.getTelefono(), pointer.getCorreo());
            pointer = pointer.next;
        }
        System.out.println();
    }

}
