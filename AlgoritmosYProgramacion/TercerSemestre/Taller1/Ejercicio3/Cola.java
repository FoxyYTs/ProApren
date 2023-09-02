package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio3;

public class Cola {
    Nodo cabeza, cola;

    public void encolar(String nombre, int edad, boolean embarazada) {
        Nodo nuevo = new Nodo(nombre, edad, embarazada);
        if (cabeza == null) {
            cabeza = cola = nuevo;
        } else {
            Nodo temp = cola;
            cola = temp.next = nuevo; 
            nuevo.back = temp;
        }
    }

    public Nodo desencolar() {
        if (cabeza == null) {
            return null;
        }
        
        Nodo cAtendido = cabeza;
        cabeza = cabeza.next;
        cabeza.back = null;
        if (cabeza == null) {
            cola = null;
        }
        return cAtendido;
    }

    public void cambiarPrioridad(String nombre) {
        if (cabeza == null){
            System.out.println("Cola Vacia");
        }
        if (cabeza.nombre.equals(nombre)){
            cabeza = cabeza.next;
            cabeza.back = null;
            return;
        }
        Nodo pointer = cabeza;
        while (!pointer.next.nombre.equals(nombre) && pointer.next != null) {
            pointer = pointer.next;
        }
        if (pointer.next != null) {
            pointer.back.next = pointer.next;
            pointer.next.back = pointer.back;
        }
        return;
    }

    public void eliminarCola() {
        cabeza = cola = null;
    }

    public void print() {
        Nodo pointer = cabeza;
        while (pointer != null) {
            System.out.println("Nombre: " + pointer.nombre + " Edad: " + pointer.edad + " Embarazo: " + pointer.embarazada);
            pointer = pointer.next; 
        }
    }
}
