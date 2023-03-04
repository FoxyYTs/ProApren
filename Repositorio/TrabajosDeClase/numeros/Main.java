package Repositorio.TrabajosDeClase.numeros;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Funciones conv = new Funciones();
        int valor,opcion;
        boolean x = true;

        try {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } catch (Exception e){

        }

        System.out.print("Ingrese el numero que quiera convertir: ");
        valor = Integer.parseInt(leer.nextLine());

        while (x) {
            System.out.println("En que base esta escrito este numero\n1) Decimal\n2) Binario\n3) Octal\n4) Hexadecimal\n5) Cerrar Programa");
            opcion = Integer.parseInt(leer.nextLine());
            
            switch (opcion) {
                case 1:
                    System.out.println("El numero " + valor + " es en base Decimal");
                    x = true;  
                    break;
    
                case 2:
                    System.out.println("El numero " + valor + " es en base Binario");
                    x = true;
                    break;
                
                case 3:
                    System.out.println("El numero " + valor + " es en base Octal");
                    x = true;
                    break;
                
                case 4:
                    System.out.println("El numero " + valor + " es en base Hexadecimal");
                    x = true;
                    break;

                case 5:
                    System.out.println("Cerrando Programa...");
                    break;
            
                default:
                    System.out.println("Opcion no valida");
                    x = true;
                    break;
            }
        }
    }
}
