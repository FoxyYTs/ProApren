package AlgoritmosYProgramacion.SegundoSemestre.Pilas;

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
    

    public void insertarC() {
        Nodo pointer1 = top1, pointer2 = top2;
        for (int i = 0; pointer1 != null || pointer2 != null ; i++) {
            if (i%2 == 0) {
                Nodo nuevo = new Nodo(pointer2.a);
                if (top3 == null) {
                    top3 = nuevo;
                } else {
                    top3.back = nuevo;
                    nuevo.next = top3;
                    top3 = top3.back;
                }
                pointer2 = pointer2.next;
            } else {
                Nodo nuevo = new Nodo(pointer1.a);
                if (top3 == null) {
                    top3 = nuevo;
                } else {
                    top3.back = nuevo;
                    nuevo.next = top3;
                    top3 = top3.back;
                }
                pointer1 = pointer1.next;
            }
        }
    }

    public void insertarD() {
        Nodo pointer = top3;
        while (pointer != null) {
            Nodo nuevo = new Nodo(pointer.a);
            if (top4 == null) {
                top4 = nuevo;
            } else {
                top4.back = nuevo;
                nuevo.next = top4;
                top4 = top4.back;
            }
            pointer = pointer.next;
        }
    }

    public void mostrarA() {
        System.out.print("Mostrar: ");
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
        System.out.print("Mostrar: ");
        Nodo pointer = top2;
        while (pointer != null) {
            System.out.print(pointer.a + " ");
            pointer = pointer.next;
        }
        System.out.println();
        System.out.println("Top: " + top2.a);

        System.out.println("================");
    }

    public void mostrarC() {
        System.out.print("Mostrar: ");
        Nodo pointer = top3;
        while (pointer != null) {
            System.out.print(pointer.a + " ");
            pointer = pointer.next;
        }
        System.out.println();
        System.out.println("Top: " + top3.a);

        System.out.println("================");
    }

    public void mostrarD() {
        System.out.print("Mostrar: ");
        Nodo pointer = top4;
        while (pointer != null) {
            System.out.print(pointer.a + " ");
            pointer = pointer.next;
        }
        System.out.println();
        System.out.println("Top: " + top4.a);

        System.out.println("================");
    }

    public void mostrarAyB() {
        System.out.println("Mostrar: ");
        Nodo pointer1 = top1, pointer2 = top2;
        for (int i = 0; pointer1 != null || pointer2 != null ; i++) {
            if (i%2 == 0) {
                System.out.println(pointer2.a + " ");
                pointer2 = pointer2.next;
            } else {
                System.out.println(pointer1.a + " ");
                pointer1 = pointer1.next;
            }
        }
    }
}
