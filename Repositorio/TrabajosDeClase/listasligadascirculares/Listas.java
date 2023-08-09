package TrabajosDeClase.listasligadascirculares;

public class Listas {
    private static Nodo cabeza;
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
        if(cabeza == null){
            return;
        }
        System.out.println("Mostrar: ");
        Nodo actual = cabeza;
        mostrarrecu(actual);;

        System.out.println();
        System.out.println("Cabeza: " + cabeza.dato + " Cola: " + cola.dato);
    }

    public static void mostrarrecu(Nodo actual){
        System.out.print(actual.dato + " ");
        if (actual.siguiente != cabeza){
            mostrarrecu(actual.siguiente);
        }
        
    }

    public void mostrars() {
        if(cabeza == null){
            return;
        }
        Nodo actual = cabeza;
        for (int i = 0; i < 20; i++) {
            System.out.print(actual.dato + " ");
            actual = actual.siguiente;
        }

        System.out.println();
        System.out.println("Cabeza: " + cabeza.dato + " Cola: " + cola.dato);
    }

    public void mostrarsinv() {
        if(cabeza == null){
            return;
        }
        Nodo actual = cola;
        for (int i = 0; i < 20; i++) {
            System.out.print(actual.dato + " ");
            actual = actual.atras;
        }

        System.out.println();
        System.out.println("Cabeza: " + cabeza.dato + " Cola: " + cola.dato);
    }

    public void eliminar(String dato) {
        Nodo actual = cabeza;
        while(!actual.dato.equals(dato)){
            actual = actual.siguiente;
        }
        if (cabeza.dato.equals(dato)){
            cabeza = cabeza.siguiente;
        }
        if (cola.dato.equals(dato)){
            cola = cola.atras;
        }
        if (actual != null){
            actual.atras.siguiente = actual.siguiente;
            actual.siguiente.atras = actual.atras;
        }
        
    }
}
