package Repositorio.ProyectoSegundoSemestre;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Agenda agenda = new Agenda();
        Scanner leer = new Scanner(System.in);

        boolean seguir = true;
        int opcion = 0;

        System.out.println("Bienvenido al programa Agenda");

        while(seguir){
            System.out.println("Que quieres hacer con la agenda ?\n1) Contactos\n2) Grupos\n3) Calendario\n4) Configuracion\n#) Cerrar Programa");
            opcion = Integer.parseInt(leer.nextLine());
            switch (opcion) {
                case 1:
                    
                    break;

                case 2:
                    
                    break;

                case 3:
                    
                    break;

                case 4:
                    
                    break;

                case 5:
                    System.out.print("\033[H\033[2J");
                    System.out.flush();

                    System.out.println("Cerrando Programa");
                    seguir = false;

                    System.out.println("Precione enter para continuar");
                    leer.nextLine();
                    break;
            
                default:
                    break;
            }
        }
    }
}
