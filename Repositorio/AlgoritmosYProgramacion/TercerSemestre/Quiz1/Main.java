package AlgoritmosYProgramacion.TercerSemestre.Quiz1;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Funciones fun = new Funciones();
    
        int opcion1, seleccionPeli, pelicula;
        String nombre, tipoAsiento;
        boolean seguir = true;

        while (seguir) {
            System.out.flush();
            System.out.print("\033[H\033[2J");
            System.out.println("MENU 1\n1) Reservar asiento.\n2. Mostrar ocupacion sala.\n3. Consultar reserva.");
            opcion1=Integer.parseInt(leer.nextLine());

        
            if(opcion1==1){
                System.out.print("\033[H\033[2J");
                System.out.flush();
                System.out.println("MENU 1.1. RESERVA.");
                System.out.print("\033[H\033[2J");
                System.out.flush();
                System.out.println("MENU 1.1. SELECCION PELICULA\n1) Gran Turismo PoliSpeed-JIC\n2) PoliNinja Turtles \u2013 Caos Mutante");
                pelicula=Integer.parseInt(leer.nextLine());
                if (pelicula == 1) {
                    System.out.println("A2-3-4 Movilidad reducida\nB0-6 C0-6 Descuento 10%\nC2-3-4 Sonido y Vibracion");
                } else if(pelicula ==2) {
                    System.out.println("A2-3-4 Movilidad reducida\nA0-6 Descuento 10%\nB2-3-4 C1-2-3-4-5 Sonido y Vibracion");
                } else {
                    System.out.println("Opcion no valida");
                }
                tipoAsiento=leer.nextLine();
                System.out.print("Ingrese el nombre del cliente: ");
                nombre = leer.nextLine();

                fun.reseva(pelicula, tipoAsiento, nombre);

            }else if(opcion1==2){
                System.out.print("\033[H\033[2J");
                System.out.flush();
                System.out.println("MENU 2.1. MOSTRAR OCUPACION SALA.\n1. SALA 1.\n2. SALA 2.");
            }else if(opcion1==3){
                System.out.print("\033[H\033[2J");
                System.out.flush();
                System.out.println("MENU 3.1. CONSULTAR RESERVA.\n1. Escriba la ubicacion de su reserva.");
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
