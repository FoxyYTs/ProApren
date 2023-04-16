public class Grupos extends Agenda{

    private String nombre;
    public Contactos head;
    public Contactos pointer = head;
    public Grupos next;

    public void insertarContacto(String nombre, String apellido, String correo, String telefono) {
        Contactos nuevo = new Contactos(nombre, apellido, correo, telefono);
        if (head == null) {
            head = nuevo;
        } else {
            Contactos pointer = head;
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
        Contactos pointer = head;
        while (pointer.next.getNombre() != nombre && pointer.next != null) {
            pointer = pointer.next;
        }
        if (pointer.next != null) {
            pointer.next = pointer.next.next;
        }
    }

    public void mostrarContacto() {
        Contactos pointer = head;
        while (pointer != null) {
            configuracion.gruposMostrarContactos(pointer.getNombre(), pointer.getApellido(), pointer.getTelefono(), pointer.getCorreo());
            pointer = pointer.next;
        }
        System.out.println();
    }

    public Grupos(String nombre) {
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
}