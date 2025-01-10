package AlgoritmosYProgramacion.TercerSemestre.Matriz2;

import java.util.Scanner;

public class Funciones {
    Scanner leer = new Scanner(System.in);
    int x = 2;
    int matriz1[][] = new int[x][x], matriz2[][] = new int[x][x];

    public void vacio(boolean full1, boolean full2){
        if(!full1 && !full2){
            System.out.println("Primero llene las matrizes para poder continuar");
        } else if (!full1 && full2){
            System.out.println("Aun no llenas la Matriz 1");
        } else if (full1 && !full2){
            System.out.println("Aun no llenas la Matriz 2");
        }
    }

    public void print(){
    System.out.println("\t\t            Matriz 1 \t\t\t\t\t\t\t\t            Matriz 2\n");
        for (int i = 0; i < matriz1.length; i++) {
            System.out.print("|\t");
            for (int j = 0; j < matriz1.length; j++) {
                System.out.print(matriz1[i][j] + "\t|\t");
            }
            System.out.print(" \t|\t");
            for (int j = 0; j < matriz1.length; j++) {
                System.out.print(matriz2[i][j] + "\t|\t");
            }
        System.out.println("\n");
        }
    }

    public void llenar(String matriz){
        if (!matriz.equals("1") && !matriz.equals("2")) {
            System.out.println("Valor no valido");
            return;
        }
        int elemento;
        for (int i = 0; i < matriz1.length; i++) {
            for (int j = 0; j < matriz1.length; j++) {
                System.out.print("Ingresa elemento: ");
                elemento = Integer.parseInt(leer.nextLine());
                if (matriz.equals("1")) {
                    matriz1[i][j] = elemento;
                } else if (matriz.equals("2")){
                    matriz2[i][j] = elemento;
                }
            }
        }
        System.out.println("Terminaste de llenar la Matriz");
    }

    public void sumaFila(){
        for (int i = 0; i < matriz1.length; i++) {
            System.out.print("|\t");
            for (int j = 0; j < matriz1.length; j++) {
                System.out.print(matriz1[i][j] + matriz2[i][j] + "\t|\t");
            }
            System.out.println("\n");
        }
    }

    public void sumaColumna(){
        for (int i = 0; i < matriz1.length; i++) {
            System.out.print("|\t");
            for (int j = 0; j < matriz1.length; j++) {
                System.out.print(matriz1[j][i] + matriz2[j][i] + "\t|\t");
            }
            System.out.println("\n");
        }
    }
}
