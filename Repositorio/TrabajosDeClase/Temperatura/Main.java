package Repositorio.TrabajosDeClase.Temperatura;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Temperatura operacion = new Temperatura();

        try {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } catch (Exception e){

        }

        int temp = 0, opcion = 0;
        System.out.print("Ingrese el valor de la temperatura que quiera convertir: ");
        temp = Integer.parseInt(leer.nextLine());

        System.out.println("Ingrese una opcion\n1) Kelvin a Celcius\n2) Kelvin a Farenheit\n3) Farenheit a Kelvin\n4) Farenheit a Celcius\n5) Celcius a Kelvin\n6) Celcius a Farenheit");
        opcion = Integer.parseInt(leer.nextLine());

        if (opcion == 1){
            System.out.println("El resultado de Kelvin a Celcius es: " + operacion.KaC(temp));
        }else if (opcion == 2){
            System.out.println("Eal resultado de Kelvin a Farenheit es: " + operacion.KaF(temp));
        }else if (opcion == 3){
            System.out.println("El resultado de Farenheit a Kelvin es: " + operacion.FaK(temp));
        }else if (opcion == 4){
            System.out.println("El resultado de Farenheit a Celcius es: " + operacion.FaC(temp));
        }else if (opcion == 5){
            System.out.println("El resultado de Celcius a Kelvin es: " + operacion.CaK(temp));
        }else if (opcion == 6){
            System.out.println("El resultado de Celcius a Farenheit es: " + operacion.CaF(temp));
        }else{
            System.out.println("Opcion no valida");
        }
    }
}
