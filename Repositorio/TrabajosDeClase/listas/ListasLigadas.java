package Repositorio.TrabajosDeClase.listas;

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
            while (actual.siguiente != null) {
                actual = actual.siguiente;
            }
            actual.siguiente = nuevo;
        }
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
