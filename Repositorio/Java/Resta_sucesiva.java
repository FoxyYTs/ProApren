import java.util.Scanner;

public class Resta_sucesiva{
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int victima = leer.nextInt(), restante = leer.nextInt(), restos,i;
        
        restos = victima;
        for (i = 0; restos >= restante; i++) {
            restos-=restante;
        }
        System.out.println("Restas "+(victima/restante));
        System.out.println("Modulo "+(victima%restante));
        System.out.println("Restas "+(i));
        System.out.println("Modulo "+(restos));
    }
}