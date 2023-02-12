import java.util.Scanner
public class Nomina {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Cuantos Trabajadores va a evaluar");
        int trabajador = scan.nextInt();
        System.out.println("Cuanto Valen las horas?");
        int vh = scan.nextInt();

        int num;
        for(num = 0; num < trabajador; ++num) {
            System.out.println("Como se llama el trabajador ?");
            String name = scan.next();
            System.out.println("Cuantas horas a trabajado");
            int h = scan.nextInt();
            int subtotal = h * vh;
            short boni;
            if (h > 48) {
                boni = 10000;
                System.out.println("Pedro a ganado una bonificacion de " + boni);
            } else {
                boni = 0;
            }

            int total = subtotal + boni;
            System.out.println("El trabajador " + name + " a Ganado " + subtotal + " mas la bonificacion seria " + total);
        }

        num = scan.nextInt();
        System.out.println(num);
    }
}
