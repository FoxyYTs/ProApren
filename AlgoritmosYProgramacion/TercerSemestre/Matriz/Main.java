package AlgoritmosYProgramacion.TercerSemestre.Matriz;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Funciones fun = new Funciones();

        fun.inicio();

        String opcion = "",bus;
        int fila = 1, columna = 1, piso = (int) (Math.floor(Math.random()*2+1));;


        while (!opcion.equals("4")) {
            System.out.flush();
            System.out.print("\033[H\033[2J");
            System.out.println("Bienvenido Al\n\tExpreso-Poli\n1) Comprar Tiquete\n2) Mostrar Ocupacion B1\n3) Mostrar Ocupacion B2\n4) Cerrar");
            opcion = leer.nextLine();
            if (opcion.equals("1")) {
                System.out.println("Selecciona el Bus\n1) Bus Basico\n2) Bus 2 pisos");
                bus = leer.nextLine();
                if (bus.equals("1")){
                    System.out.println("Puestos\n1) Seleccionar puesto\n2) Asignar Aleatorio");
                    opcion = leer.nextLine();
                    if (opcion.equals("1")) {
                        fun.mapaB1();
                        System.out.print("\n\nEscribe el numero de la fila: ");
                        fila = Integer.parseInt(leer.nextLine());
                        System.out.print("\nEscribe el NUMERO de la columna: ");
                        columna = Integer.parseInt(leer.nextLine());
                        if (!fun.Ocupar1(fila,columna)) {
                            System.out.println("El asiento que elegiste esta ocupado");
                            leer.nextLine();
                            continue;
                        }
                        leer.nextLine();
                    } else if (opcion.equals("2")) {
                        while (!fun.Ocupar1(fila, columna)) {
                            if (!fun.Ocupar1(fila, columna)){
                                fila = (int) (Math.floor(Math.random()*4+1));
                                columna = (int) (Math.floor(Math.random()*9+1));
                            }
                        }
                    }
                } else if (bus.equals("2")){
                    System.out.println("Puestos\n1) Seleccionar puesto\n2) Asignar Aleatorio");
                    opcion = leer.nextLine();
                    if (opcion.equals("1")) {
                        fun.mapaB2();
                        System.out.println("\n\nEscribe el numero de PISO");
                        piso = Integer.parseInt(leer.nextLine());
                        System.out.print("\nEscribe el numero de la FILA: ");
                        fila = Integer.parseInt(leer.nextLine());
                        System.out.print("\nEscribe el numero de la COLUMNA: ");
                        columna = Integer.parseInt(leer.nextLine());
                        if (!fun.Ocupar2(piso, fila, columna)) {
                            System.out.println("El asiento que elegiste esta ocupado");
                            leer.nextLine();
                            continue;
                        }
                        leer.nextLine();
                    } else if (opcion.equals("2")) {
                        while (!fun.Ocupar2(piso, fila, columna)) {
                            if (!fun.Ocupar2(piso ,fila, columna)){
                                piso = (int) (Math.floor(Math.random()*2+1));
                                if (piso == 1){
                                    fila = (int) (Math.floor(Math.random()*2+1));
                                    columna = (int) (Math.floor(Math.random()*9+1));
                                } else {
                                    fila = (int) (Math.floor(Math.random()*4+1));
                                    columna = (int) (Math.floor(Math.random()*5+1));
                                }
                            }
                        }
                    }
                } else if (!bus.equals("1") && !bus.equals("2")) {
                    System.out.println("Opcion no valida");
                    leer.nextLine();
                    continue;
                }
            } else if (opcion.equals("2")){
                System.out.flush();
                System.out.print("\033[H\033[2J");
                fun.mapaB1();
                leer.nextLine();
            } else if (opcion.equals("3")){
                System.out.flush();
                System.out.print("\033[H\033[2J");
                fun.mapaB2();
                leer.nextLine();    
            } else if (opcion.equals("4")){
                System.out.println("Cerrando...");
                leer.nextLine();
            }
        }
    }
}
