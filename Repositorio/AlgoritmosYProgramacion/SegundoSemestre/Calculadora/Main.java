package TrabajosDeClase.Calculadora;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Calculadora proceso = new Calculadora();

        int a = 0, b = 0, opcion = 0;
        System.out.print("ingresa un numero: ");
        a = Integer.parseInt(leer.nextLine());
        System.out.print("ingresa otro numero");
        b = Integer.parseInt(leer.nextLine());

        System.out.println("Ingresa que opcion quieres\n1) Suma\n2) Resta \n3) Multiplicacion\n4 Divicion");
        opcion = Integer.parseInt(leer.nextLine());
        if (opcion == 1) {
            System.out.println("La Suma es: " + proceso.sumar(a, b));  
        }else if(opcion == 2){
            System.out.println("La Resta es: " + proceso.restar(a, b));
        }else if(opcion == 3){
            System.out.println("La Multiplicacion es: " + proceso.multiplicar(a, b));
        }else if(opcion == 4){
            System.out.println("La Divicion es: " + proceso.dividir(a, b));
        }else{
            System.out.println("La opcion no es correcta");
        }
    }
}
