package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos1;

public class Conjunto {
    private Nodo head;
    private Nodo tail;

    public Conjunto(){
        this.head = null;
        this.tail = null;
    }

    public void insertar(String dato){
        Nodo nuevo = new Nodo(dato);
        if (head == null){
            head = nuevo;
            tail = nuevo;
        } else {
            tail.setNext(nuevo);
            tail = tail.getNext();
        }
    }

    public Nodo getHead(){
        return head;
    }

    public void pertenece(String dato){
        Nodo pointer = head;
        while (pointer != null){
            if (pointer.getDato().equals(dato)){
                System.out.println("El dato " + dato + " pertenece al conjunto");
                return;
            }
            pointer = pointer.getNext();
        }
        System.out.println("El dato " + dato + " no pertenece al conjunto");
    }

    

    public void mostrar() {
        System.out.println("Mostrar: ");
        Nodo pointer = head;
        while (pointer != null) {
            System.out.print(pointer.getDato() + " ");
            pointer = pointer.getNext();
        }
        System.out.println();
        System.out.println("Cabeza: " + head.getDato() + " Cola: " + tail.getDato());
    }
}
