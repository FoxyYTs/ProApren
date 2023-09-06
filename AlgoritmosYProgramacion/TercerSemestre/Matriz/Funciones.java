package AlgoritmosYProgramacion.TercerSemestre.Matriz;

public class Funciones {
    String bus1[][] = new String[5][10], bus2p1[][] = new String[2][7], bus2p2[][] = new String[4][5];

    public void inicio(){
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 10; j++) {
                if (i == ) {
                    
                }
            }
        }

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 7; j++) {
                bus2p1[i][j] = "|O|";
            }
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                bus2p2[i][j] = "|O|";
            }
        }
    }

    public void mapaB1(){
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(bus1[i][j]);
            }
            if (i == 1) {
                System.out.println();
            }
            System.out.println();
        }
        System.out.println("|O| = VACIO\n|X| = OCUPADO");
    }

    public void mapaB2(){
        System.out.println("Piso 1");
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.print(bus2p1[i][j]);
            }
            if (i == 0) {
                System.out.println();
            }
            System.out.println();
        }
        System.out.println("\nPiso 2");

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(bus2p2[i][j]);
            }
            if (i == 1) {
                System.out.println();
            }
            System.out.println();
        }
        System.out.println("|O| = VACIO\n|X| = OCUPADO");
    }
}
