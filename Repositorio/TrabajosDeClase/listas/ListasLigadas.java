package TrabajosDeClase.listas;

public class ListasLigadas {
    private Nodo cabeza;

    Nodo nuevo = new Nodo(1);

    public ListasLigadas() {
        this.cabeza = null;
    }
    
    public void insertar(int dato) {
        Nodo nuevo = new Nodo(dato);
        if (cabeza == null) {
            cabeza = nuevo;
        } else {
            Nodo actual = cabeza;
            
            recorrer(actual);
            actual.siguiente = nuevo;
        }
    }

    public static Nodo recorrer(Nodo actual){
        if(actual.siguiente != null){
            recorrer(actual);
            actual = actual.siguiente;
        }
        return actual;
    }
    
    public void mostrar() {
        Nodo actual = cabeza;
        while (actual != null) {
            System.out.print(actual.dato + " ");
            actual = actual.siguiente;
        }
        System.out.println();
    }
}
