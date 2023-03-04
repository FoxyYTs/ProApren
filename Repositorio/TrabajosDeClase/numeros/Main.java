package Repositorio.TrabajosDeClase.numeros;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Funciones conv = new Funciones();
        int valor,opcionA = 0,opcionB = 0;
        boolean x = true;

        try {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } catch (Exception e){

        }

        

        while (x) {
            System.out.print("Ingrese el numero que quiera convertir: ");
            valor = Integer.parseInt(leer.nextLine());

            System.out.println("En que base esta escrito este numero?\n1) Decimal\n2) Binario\n3) Octal\n4) Hexadecimal\n5) Cerrar Programa");
            opcionA = Integer.parseInt(leer.nextLine());
            
            switch (opcionA) {
                case 1:
                    System.out.println("El numero " + valor + " es en base Decimal");
                    opcionB = destino(opcionA);
                    break;
    
                case 2:
                    System.out.println("El numero " + valor + " es en base Binario");
                    opcionB = destino(opcionA);
                    break;
                
                case 3:
                    System.out.println("El numero " + valor + " es en base Octal");
                    opcionB = destino(opcionA);
                    break;
                
                case 4:
                    System.out.println("El numero " + valor + " es en base Hexadecimal");
                    opcionB = destino(opcionA);
                    break;

                case 5:
                    System.out.println("Cerrando Programa...");
                    x = false;
                    break;
            
                default:
                    System.out.println("Opcion no valida");
                    x = true;
                    break;
            }
        }
        
    }
    public static int destino(int a){
        Scanner leer = new Scanner(System.in);
        String bases[] = {"Decimal","Binario","Octal", "Hexadecimal"};
        System.out.println("A que base lo quieres convertir?\n1) Decimal\n2) Binario\n3) Octal\n4) Hexadecimal\n5) Cerrar Programa");
        int opcion = Integer.parseInt(leer.nextLine());
        switch (opcion) {
            case 1:
                System.out.println("Vas a convertir un numero de Base " + bases[a-1] + " a Base Decimal");
                break;

            case 2:
                System.out.println("Vas a convertir un numero de Base " + bases[a-1] + " a Base Binario");
                break;

            case 3:
                System.out.println("Vas a convertir un numero de Base " + bases[a-1] + " a Base Octal");
                break;

            case 4:
                System.out.println("Vas a convertir un numero de Base " + bases[a-1] + " a Base Hexadecimal");
                break;

            default:
                System.out.println("Opcion no valida");
                opcion = 0;


        }
        return opcion;
        
    }
}
