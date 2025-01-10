package AlgoritmosYProgramacion.TercerSemestre.Triqui;

import java.util.Scanner;

public class Tablero {
    private static Scanner leer = new Scanner(System.in);
    private final int X = 4;
    private String triqui[][] = new String[X][X], toca;
    private int posX, posY, turno = 0;
    private boolean gano = false;
    public void juego(){
        inicio();
        
        while (turno < 9 && !gano) {
            clearConsole();
            print();
            gano();
            if (gano) {
                return;
            }
            System.out.print("COLUMNA: ");
            posX = Integer.parseInt(leer.nextLine());
            System.out.print("FILA:");
            posY = Integer.parseInt(leer.nextLine());
            jugada();
        }
        
        
    }
    private void clearConsole() {
            System.out.flush();
            System.out.print("\033[H\033[2J");
        }
    private void jugada(){
        if (triqui[posY][posX].equals("| |")) {
            turno++;
            triqui[posY][posX] = "|" + toca + "|";
        }
    }
    private void gano(){
        for (int i = 1; i < X; i++) {
            if (triqui[i][2].equals(triqui[i][1]) && triqui[i][2].equals(triqui[i][3]) && !triqui[i][2].equals("| |")) {
                System.out.println("Gano la: " + triqui[i][2]);
                gano = true;
                return;
            }
        }
        for (int i = 1; i < X; i++) {
            if (triqui[2][i].equals(triqui[1][i]) && triqui[2][i].equals(triqui[3][i]) && !triqui[2][i].equals("| |")) {
                System.out.println("Gano la: " + triqui[1][i]);
                gano = true;
                return;
            }
        }
        if (triqui[2][2].equals(triqui[1][1]) && triqui[2][2].equals(triqui[3][3]) && !triqui[2][2].equals("| |")) {
            System.out.println("Gano la: " + triqui[2][2]);
            gano = true;
            return;
        }
        if (triqui[2][2].equals(triqui[3][1]) && triqui[2][2].equals(triqui[1][3]) && !triqui[2][2].equals("| |")) {
            System.out.println("Gano la: " + triqui[2][2]);
            gano = true;
            return;
        }
    }

    private void inicio(){
        for (int i = 0; i < X; i++) {
            for (int j = 0; j < X; j++) {
                if (j == 0 && i == 0) {
                    triqui[i][j] = "X  ";
                } else if (j == 0) {
                    triqui[i][j] = i + " ";
                } else if (i == 0){
                    triqui[i][j] = j + "  ";
                } else {
                    triqui[i][j] = "| |";
                }
            }
        }
    }

    public void print(){
        if (turno % 2 == 0){
            toca = "X";
            triqui[0][0] = "X  ";
        } else if (turno % 2 != 0){
            toca = "O";
            triqui[0][0] = "O  ";
        }
        for (int i = 0; i < X; i++) {
            for (int j = 0; j < X; j++) {
                System.out.print(triqui[i][j]);
            }
            System.out.println();
        }
    }
}
