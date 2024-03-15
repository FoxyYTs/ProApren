package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos1;

public class Conjunto {
    private Nodo head;
    private Nodo tail;

    public Conjunto(){
        this.head = null;
        this.tail = null;
    }

    public Nodo getHead(){
        return head;
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

    public static Nodo pertenece(Nodo head,String dato){
        Nodo pointer = head;
        while (pointer != null){
            if (pointer.getDato().equals(dato)){
                return pointer;
            }
            pointer = pointer.getNext();
        }
        return null;
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

    public static Conjunto union(Conjunto cnjto1, Conjunto cnjto2) {
        Conjunto conjunto = new Conjunto();
        Nodo pointer1 = cnjto1.getHead();
        Nodo pointer2 = cnjto2.getHead();

        while (pointer1 != null) {
            Nodo encontrado = Conjunto.pertenece(conjunto.getHead(), pointer1.getDato());
            if (encontrado == null) {
                conjunto.insertar(pointer1.getDato());
            }

            pointer1 = pointer1.getNext();
        }
        while (pointer2 != null) {
            Nodo encontrado = Conjunto.pertenece(conjunto.getHead(), pointer2.getDato());
            if (encontrado == null) {
                conjunto.insertar(pointer2.getDato());
            }

            pointer2 = pointer2.getNext();
        }
        System.out.println("Union");
        conjunto.mostrar();
        return conjunto;
    }

    public void difSimetrica(){
    }

    public static Conjunto diferenciaSimetrica(Conjunto lista1, Conjunto lista2) {
        Conjunto diferencia = new Conjunto();
        Nodo actualLista1 = lista1.getHead();
        Nodo actualLista2 = lista2.getHead();

        while (actualLista1 != null) {
            Nodo encontrado = Conjunto.pertenece(lista2.getHead(), actualLista1.getDato());
            if (encontrado == null) {
                diferencia.insertar(actualLista1.getDato());
            }
            actualLista1 = actualLista1.getNext();
        }
        while (actualLista2 != null) {
            Nodo encontrado = Conjunto.pertenece(lista1.getHead(), actualLista2.getDato());
            if (encontrado == null) {
                diferencia.insertar(actualLista2.getDato());
            }

            actualLista2 = actualLista2.getNext();
        }
        System.out.println("Diferencia simetrica");
        diferencia.mostrar();
        return diferencia;
    }
}
