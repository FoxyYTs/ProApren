package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos2;

public class Funciones {
    private Nodo head;
    static int canStud = 0;

    public Funciones(){
        this.head = null;
    }

    public Nodo getHead(){
        return head;
    }

    public void union(Funciones fun1, Funciones fun2) {
        Funciones conjunto = new Funciones();
        Nodo pointer1 = fun1.getHead();
        Nodo pointer2 = fun2.getHead();

        while (pointer1 != null) {
            Nodo encontrado = Funciones.pertenece(conjunto.getHead(), pointer1.getName());
            if (encontrado == null) {
                conjunto.insert(pointer1);
            }
            pointer1 = pointer1.getNext();
        }
        while (pointer2 != null) {
            Nodo encontrado = Funciones.pertenece(conjunto.getHead(), pointer2.getName());
            if (encontrado == null) {
                conjunto.insert(pointer2);
            }
            pointer2 = pointer2.getNext();
        }
        System.out.println("Union");
        conjunto.mostrar();
    }

    public static Nodo pertenece(Nodo head,String name){
        Nodo pointer = head;
        while (pointer != null){
            if (pointer.getName().equals(name)){
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
            System.out.print(pointer.getName() + " ");
            pointer = pointer.getNext();
        }
        System.out.println();
        System.out.println("Cabeza: " + head.getName());
    }

    public void insert(Nodo nuevo){
        if (head == null) {
            head = nuevo;
        } else {
            Nodo pointer = head;
            while(pointer.getNext() != null){
                pointer = pointer.getNext();
            }
            pointer.setNext(nuevo);
        }
    }

    
}
