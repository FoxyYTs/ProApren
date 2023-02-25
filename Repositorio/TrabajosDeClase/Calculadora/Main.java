package Repositorio.TrabajosDeClase.Calculadora;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Calculadora proceso = new Calculadora();

        int a = 0, b = 0, opcion = 0;
        System.out.print("ingresa un numero: ");
        a = Integer.parseInt(leer.nextLine());
        System.out.println("ingresa otro numero");
        b = Integer.parseInt(leer.nextLine());

        System.out.println("Ingresa que opcion quieres\n1) Suma\n2) Resta \n3) Multiplicacion\n4 Divicion");
            if (opcion == 1) {
                System.out.println();
                
            }
    }
}
