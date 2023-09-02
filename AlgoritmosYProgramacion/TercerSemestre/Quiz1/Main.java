package AlgoritmosYProgramacion.TercerSemestre.Quiz1;

import java.util.Scanner;

public class Main {

    /*Jose Andres Daza Gallego
     Cristian Camilo Grajales Serna */

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Funciones fun = new Funciones();

        fun.inicio();

        int opcion1, pelicula, columna;
        String nombre, fila;
        boolean seguir = true;

        while (seguir) {
            System.out.flush();
            System.out.print("\033[H\033[2J");
            System.out.println("MENU 1\n1) Reservar asiento\n2) Mostrar ocupacion sala\n3) Consultar reserva\n4) Cerrar");
            opcion1=Integer.parseInt(leer.nextLine());

        
            if(opcion1==1){
                System.out.print("\033[H\033[2J");
                System.out.flush();
                System.out.println("SELECCION PELICULA\n1) Gran Turismo PoliSpeed-JIC\n2) PoliNinja Turtles 2013 Caos Mutante");
                pelicula=Integer.parseInt(leer.nextLine());
                if (pelicula == 1) {
                    System.out.print("\033[H\033[2J");
                    System.out.flush();
                    fun.mapaSala1();
                    System.out.println("\n");
                    System.out.println("\n|X| = Ocupado\n|G| = General\n|S| = Sonido y Vibracion\n|M| = Movilidad Reducida");
                } else if(pelicula ==2) {
                    fun.mapaSala2();
                    System.out.println("\n");
                    System.out.println("\n|X| = Ocupado\n|G| = General\n|S| = Sonido y Vibracion\n|M| = Movilidad Reducida");
                } else {
                    System.out.println("Opcion no valida");
                }
                System.out.print("\n\nEscribe la LETRA de la fila: ");
                fila = leer.nextLine();
                System.out.print("\nEscribe el NUMERO de la columna: ");
                columna = Integer.parseInt(leer.nextLine());
                System.out.print("\nIngrese el nombre del cliente: ");
                nombre = leer.nextLine();

                fun.reseva(pelicula, fila, columna , nombre);
                leer.nextLine();

            }else if(opcion1 == 2){
                System.out.print("\033[H\033[2J");
                System.out.flush();
                System.out.println("MOSTRAR OCUPACION SALA.\n1) SALA 1.\n2) SALA 2.");
                pelicula=Integer.parseInt(leer.nextLine());
                if (pelicula == 1) {
                    fun.mapaSala1();
                } else if (pelicula == 2){
                    fun.mapaSala2();
                }
                System.out.println("\n");
                System.out.println("\n|X| = Ocupado\n|G| = General\n|S| = Sonido y Vibracion\n|M| = Movilidad Reducida");
                leer.next();
            }else if(opcion1==3){
                System.out.print("\033[H\033[2J");
                System.out.flush();
                System.out.print("Que sala quieres consultar\n1) Sala 1\n2) Sala 2\n Escribe la opcion: ");
                pelicula=Integer.parseInt(leer.nextLine());
                System.out.print("\nEscribe la LETRA de la fila: ");
                fila = leer.nextLine();
                System.out.print("\nEscribe el NUMERO de la columna: ");
                columna = Integer.parseInt(leer.nextLine());

                fun.consulta(pelicula, fila, columna);

                leer.nextLine();
            }else if(opcion1==4){
                System.out.print("\033[H\033[2J");
                System.out.flush();
                System.out.println("Saliendo...");
                seguir = false;
                leer.nextLine();
            }
        }
    }
    


}
