package AlgoritmosYProgramacion.TercerSemestre.Matriz2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Funciones fun = new Funciones();

        boolean full1 = false, full2 = false, seguir = true;
        String opcion;

        while (seguir) {
            System.out.flush();
            System.out.print("\033[H\033[2J");
            fun.print();
            System.out.println("Menu de Matrices\n1) Llenar Matriz\n2) Sumar fila\n3) Sumar Columna\n4) Sumar la Diagonal\n5) Sumar la Diagonal Inversa\n6) Imprimir el promedio\n7) Cerrar");
            opcion = leer.nextLine();
            if (opcion.equals("1")) {
                System.out.flush();
                System.out.print("\033[H\033[2J");
                System.out.println("Que Matriz Quieres llenar: ");
                opcion = leer.nextLine();
                if (opcion.equals("1")) {
                    full1 = true;
                } else if (opcion.equals("2")){
                    full2 = true;
                }
                fun.llenar(opcion);
                leer.nextLine();
            } else if (opcion.equals("2")){
                System.out.flush();
                System.out.print("\033[H\033[2J");
                if (full1 && full2) {
                    fun.sumaFila();
                } else {
                    fun.vacio(full1, full2);
                }
                leer.nextLine();
            } else if (opcion.equals("3")){
                System.out.flush();
                System.out.print("\033[H\033[2J");
                if (full1 && full2) {
                    fun.sumaFila();
                } else {
                    fun.vacio(full1, full2);
                }
                leer.nextLine();
            }
        }
        leer.close();
    }
}

