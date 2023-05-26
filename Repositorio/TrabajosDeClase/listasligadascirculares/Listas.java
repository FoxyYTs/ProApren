package TrabajosDeClase.listasligadascirculares;

public class Listas {
    private Nodo cabeza;
    private Nodo cola;

    public Listas () {
        this.cabeza = null;
        this.cola = null;
    }

    public void insertar(String dato) {
        Nodo nuevo = new Nodo(dato);
        if (cabeza == null) {
            cabeza = nuevo;
            cola = nuevo;

            nuevo.siguiente = nuevo;
            nuevo.atras = nuevo;
        } else {
            Nodo actual = cola;
            cabeza.atras = cola = actual.siguiente = nuevo;
            nuevo.atras = actual;
            cola.siguiente = cabeza;
        }
    }
    
    public void mostrar() {
        System.out.println("Mostrar: ");
        Nodo actual = cabeza;
        for (int i = 0; actual != null && i < 20; i++) {
            System.out.print(actual.dato + " ");
            actual = actual.siguiente;
        }
        System.out.println();
        System.out.println("Cabeza: " + cabeza.dato + " Cola: " + cola.dato);
    }

    public void invmostrar() {
        System.out.println("Mostrar inverso: ");
        Nodo actual = cola;
        for (int i = 0; actual != null && i < 20; i++) {
            System.out.print(actual.dato + " ");
            actual = actual.atras;
        }
        System.out.println();
        System.out.println("Cabeza: " + cabeza.dato + " Cola: " + cola.dato);
    }
}
