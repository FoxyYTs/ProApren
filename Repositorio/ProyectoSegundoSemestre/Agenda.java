package Repositorio.ProyectoSegundoSemestre;

public class Agenda {
    private static Contacto hContacto;
    private static String formatoFechaHora = "dd/MM/yyyy", idioma = "es";
    public static Configuracion configuracion = new Configuracion(formatoFechaHora, idioma);

    public Agenda(){
        Agenda.hContacto = null;
    }
    
    public void menu(){
        System.out.println("creando nuevo contacto");
    }

    public static void insertarContacto(String nombre, String apellido, String correo, String telefono) {
        Contacto nuevo = new Contacto(nombre, apellido, correo, telefono);
        if (hContacto == null) {
            hContacto = nuevo;
        } else {
            Contacto pointer = hContacto;
            while (pointer.next != null) {
                pointer = pointer.next;
            }
            pointer.next = nuevo;
        }
    }

    public static void eliminarContacto(String nombre) {
        if (hContacto == null) {
            return;
        }
        if (hContacto.getNombre() == nombre) {
            hContacto = hContacto.next;
            return;
        }
        Contacto pointer = hContacto;
        while (pointer.next.getNombre() != nombre && pointer.next != null) {
            pointer = pointer.next;
        }
        if (pointer.next != null) {
            pointer.next = pointer.next.next;
        }
    }

    public static void mostrarContacto() {
        Contacto pointer = hContacto;
        while (pointer != null) {
            configuracion.gruposMostrarContactos(pointer.getNombre(), pointer.getApellido(), pointer.getTelefono(), pointer.getCorreo());
            pointer = pointer.next;
        }
        System.out.println();
    }
}
