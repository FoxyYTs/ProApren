package AlgoritmosYProgramacion.TercerSemestre.Matriz;

public class Funciones {
    String bus1[][] = new String[5][10];
    String bus2p1[][] = new String[3][10];


    String bus2p2[][] = new String[5][6];

    public void inicio(){
        for (int i = 0; i < bus1.length; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0 && i == 0) {
                    bus1[i][j] = "X  ";
                } else if (j == 0) {
                    bus1[i][j] = (char)('A' + i) + " ";
                } else if (i == 0){
                    bus1[i][j] = j + "  ";
                } else {
                    bus1[i][j] = "|O|";
                }
            }
        }

        for (int i = 0; i < bus2p1.length; i++) {
            for (int j = 0; j < 8; j++) {
                if (j == 0 && i == 0) {
                    bus2p1[i][j] = "X  ";
                } else if (j == 0) {
                    bus2p1[i][j] = (char)('A' + i) + " ";
                } else if (i == 0){
                    bus2p1[i][j] = j + "  ";
                } else {
                    bus2p1[i][j] = "|O|";
                }
            }
        }

        for (int i = 0; i < bus2p2.length; i++) {
            for (int j = 0; j < 6; j++) {
                if (j == 0 && i == 0) {
                    bus2p2[i][j] = "X  ";
                } else if (j == 0) {
                    bus2p2[i][j] = (char)('A' + i) + " ";
                } else if (i == 0){
                    bus2p2[i][j] = j + "  ";
                } else {
                    bus2p2[i][j] = "|O|";
                }
            }
        }
    }

    public void mapaB1(){
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(bus1[i][j]);
            }
            if (i == 2) {
                System.out.println();
            }
            System.out.println();
        }
        System.out.println("\n|O| = VACIO\n|X| = OCUPADO");
    }

    public void mapaB2(){
        System.out.println("Piso 1");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 8; j++) {
                System.out.print(bus2p1[i][j]);
            }
            if (i == 1) {
                System.out.println();
            }
            System.out.println();
        }
        System.out.println("\nPiso 2");

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(bus2p2[i][j]);
            }
            if (i == 2) {
                System.out.println();
            }
            System.out.println();
        }
        System.out.println("\n|O| = VACIO\n|X| = OCUPADO");
    }
}
