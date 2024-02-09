package AlgoritmosYProgramacion.SegundoSemestre.listas;

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
            while(actual.siguiente != null){
                actual = actual.siguiente;
            }
            actual.siguiente = nuevo;
        }
    }
    
    public void mostrar() {
        Nodo actual = cabeza;
        mostrarRecu(actual);
        System.out.println();
    }

    public static void mostrarRecu(Nodo actual){
        if (actual != null){
            mostrarRecu(actual.siguiente);
            System.out.println(actual.dato + " ");
        }
    }
}
