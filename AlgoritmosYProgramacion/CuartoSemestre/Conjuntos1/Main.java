package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos1;

public class Main {
    public static void main(String[] args) {
        Conjunto conjunto1 = new Conjunto();
        Conjunto conjunto2 = new Conjunto();

        System.out.print("\033[H\033[2J");
        System.out.flush();

        for (int i = 1; i <= 10; i+=2) {
            conjunto1.insertar("conjunto1 " + i);
        }
        conjunto2.insertar("asd");
        for (int i = 0; i <= 10; i+=2) {
            conjunto2.insertar("conjunto2 " + i);
        }

        conjunto1.pertenece("hola7");

        conjunto1.pertenece("hola8");

        conjunto2.pertenece("hola7");

        conjunto2.pertenece("hola8");
        
        System.out.println("Conjunto 1");
        conjunto1.mostrar();
        System.out.println("========");
        System.out.println("Conjunto 2");
        conjunto2.mostrar();

        union(conjunto1, conjunto2);

        conjunto2.mostrar();

        
    }

    public static void union(Conjunto set1, Conjunto set2){
        Nodo pointer1 = set1.getHead();
        while (pointer1 != null){
            int x = 0;
            Nodo pointer2 = set2.getHead();
            while (pointer2 != null){
                if (pointer1.getDato().equals(pointer2.getDato())){
                    x++;
                }
                System.out.println(x);
                System.out.println(pointer2.getDato());
                pointer2 = pointer2.getNext();
            }
            if (x==0){
                set2.insertar(pointer1.getDato());
            }
            pointer1 = pointer1.getNext();
        }
    }
}
