package TrabajosDeClase.listas;

public class Pedro {
    public static void main(String[] args) {
        Nodo nodo1 = new Nodo(0);
        Nodo head = nodo1;
        Nodo pointer = head;
        
        for (int i = 0; i <= 10; i++) {
            Nodo nodi = new Nodo(i);
        }

        for (int i = 0; pointer != null; i++) {
            pointer = pointer.siguiente;
            System.out.println(pointer);
        }
    }
}
