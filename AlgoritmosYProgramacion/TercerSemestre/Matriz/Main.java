package AlgoritmosYProgramacion.TercerSemestre.Matriz;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Funciones fun = new Funciones();

        fun.inicio();

        String opcion = "",bus;


        while (!opcion.equals("5")) {
            System.out.flush();
            System.out.print("\033[H\033[2J");
            System.out.println("Bienvenido Al\n\tExpreso-Poli\n1) Comprar Tiquete\n2) Mostrar Ocupacion B1\n3) Mostrar Ocupacion B2\n4) Buscar Recerva\n5) Cerrar");
            opcion = leer.nextLine();
            if (opcion.equals("1")) {
                System.out.println("Selecciona el Bus\n1) Bus Basico\n2) Bus 2 pisos");
                bus = leer.nextLine();
                if (!bus.equals("1") || !bus.equals("2")) {
                    System.out.println("Opcion no valida");
                    break;
                }
                System.out.println("Puestos\n1) Seleccionar puesto\n2) Asignar Aleatorio");
                opcion = leer.nextLine();
                if (opcion.equals("1")) {
                    
                } else if (opcion.equals("2")) {
                    
                }
            } else if (opcion.equals("2")){
                fun.mapaB1();
                leer.nextLine();
            } else if (opcion.equals("3")){
                fun.mapaB2();
                leer.nextLine();    
            } else if (opcion.equals("4")){
            } else if (opcion.equals("5")){
                System.out.println("Cerrando...");
                leer.nextLine();
            }
        }
    }
}
