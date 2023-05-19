package Repositorio.TrabajosDeClase.Pilas;

public class Pilas {
    Nodo top1,top2,top3,top4;

    public Pilas(){
        this.top1 = null;
        this.top2 = null;
        this.top3 = null;
        this.top4 = null;
    }

    public void insertarA(int dato) {
        Nodo nuevo = new Nodo(dato);
        if (top1 == null) {
            top1 = nuevo;
        } else {
            top1.back = nuevo;
            nuevo.next = top1;
            top1 = top1.back;
        }
    }

    public void insertarB(int dato) {
        Nodo nuevo = new Nodo(dato);
        if (top2 == null) {
            top2 = nuevo;
        } else {
            top2.back = nuevo;
            nuevo.next = top2;
            top2 = top2.back;
        }
    }

    public void mostrarA() {
        System.out.println("Mostrar: ");
        Nodo pointer = top1;
        while (pointer != null) {
            System.out.print(pointer.a + " ");
            pointer = pointer.next;
        }
        System.out.println();
        System.out.println("Top: " + top1.a);

        System.out.println("================");
    }
    

    public void mostrarB() {
        System.out.println("Mostrar: ");
        Nodo pointer = top2;
        while (pointer != null) {
            System.out.print(pointer.a + " ");
            pointer = pointer.next;
        }
        System.out.println();
        System.out.println("Top: " + top2.a);
    }
}
