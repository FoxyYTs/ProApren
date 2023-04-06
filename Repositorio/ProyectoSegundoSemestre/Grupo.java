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

    public void agregarContactoGrupo(Contacto conta){
        Contacto nuevo = new Contacto(conta.getNombre(), conta.getApellido(), conta.getTelefono(), conta.getCorreo());
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
    
    public void eliminarContactoGrupo(String nombre,String apellido) {
        if (head == null) {
            return;
        }
        if (head.getNombre() == nombre && head.getApellido() == apellido) {
            head = head.next;
            return;
        }
        Contacto pointer = head;
        while (pointer.next.getNombre() != nombre && pointer.next.getApellido() != apellido && pointer.next != null) {
            pointer = pointer.next;
        }
        if (pointer.next != null) {
            pointer.next = pointer.next.next;
        }
    }

    public void mostrarContactoGrupo() {
        Contacto pointer = head;
        while (pointer != null) {
            configuracion.imprimirMostrarContactos(pointer.getNombre(), pointer.getApellido(), pointer.getTelefono(), pointer.getCorreo());
            pointer = pointer.next;
        }
        System.out.println();
    }

}
