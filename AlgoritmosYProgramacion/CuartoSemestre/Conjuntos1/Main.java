package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos1;

public class Main {
    public static void main(String[] args) {
        Conjunto conjunto1 = new Conjunto();
        Conjunto conjunto2 = new Conjunto();

        System.out.print("\033[H\033[2J");
        System.out.flush();

        for (int i = 0; i <= 10; i+=1) {
            conjunto1.insertar(" "+i);
        }
        for (int i = 5; i <= 15; i+=1) {
            conjunto2.insertar(" " + i);
        }
        if (Conjunto.pertenece(conjunto1.getHead(), " 1") == null) {
            System.out.println("No pertenece");
        }else{
            System.out.println("Pertenece");}
        
        System.out.println("Conjunto 1");
        conjunto1.mostrar();
        System.out.println("========");
        System.out.println("Conjunto 2");
        conjunto2.mostrar();

        Conjunto.union(conjunto1, conjunto2);
        Conjunto.diferenciaSimetrica(conjunto1, conjunto2);
        
    }

    
}
