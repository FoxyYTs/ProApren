package AlgoritmosYProgramacion.SegundoSemestre.listasligadasdobles;

public class Primero {
    private Nodo cabeza;
    private Nodo cola;

    public Primero() {
        this.cabeza = null;
        this.cola = null;
    }
    
    public void insertar(String dato) {
        Nodo nuevo = new Nodo(dato);
        if (cabeza == null) {
            cabeza = nuevo;
            cola = nuevo;
        } else {
            Nodo actual = cabeza;
            while (actual.siguiente != null) {
                actual = actual.siguiente;
            }
            cola = actual.siguiente = nuevo;
            nuevo.atras = actual;
        }
    }

    public void eliminar(String dato) {
        if (cabeza.dato.equals(dato)){
            cabeza = cabeza.siguiente;
            cabeza.atras = null;
        }
        Nodo actual = cabeza;
        while(!actual.dato.equals(dato)){
            actual = actual.siguiente;
        }
        if (actual != null){
            actual.atras.siguiente = actual.siguiente;
            actual.siguiente.atras = actual.atras;
        }
    }
    
    public void mostrar() {
        System.out.println("Mostrar: ");
        Nodo actual = cabeza;
        while (actual != null) {
            System.out.print(actual.dato + " ");
            actual = actual.siguiente;
        }
        System.out.println();
        System.out.println("Cabeza: " + cabeza.dato + " Cola: " + cola.dato);
    }

    public void invmostrar() {
        System.out.println("Mostrar inverso: ");
        Nodo actual = cola;
        while (actual != null) {
            System.out.print(actual.dato + " ");
            actual = actual.atras;
        }
        System.out.println();
        System.out.println("Cabeza: " + cabeza.dato + " Cola: " + cola.dato);
    }
}
