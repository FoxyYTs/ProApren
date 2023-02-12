import java.util.Scanner;
public class holamundo {
    public static void main(String[] args) {
        String name;
        int h, vh, boni, subtotal, total, trabajador;
        Scanner scan = new Scanner(System.in);
        System.out.println("Cuantos Trabajadores va a evaluar");
        trabajador = scan.nextInt();
        System.out.println("Cuanto Valen las horas?");
        vh = scan.nextInt();

        for (int i = 0; i < trabajador ; i++) {

            System.out.println("Como se llama el trabajador ?");
            name = scan.next();
            System.out.println("Cuantas horas a trabajado");
            h = scan.nextInt();

            subtotal = h*vh;

            if (h > 48) {
                boni = 10000;
                System.out.println("Pedro a ganado una bonificacion de " + boni);
            }else{
                System.out.println("no a ganado una bonificacion por horas extra");
                boni = 0;
            }
            total = subtotal + boni;

            System.out.println("El trabajador "+name+" a Ganado "+ subtotal+" mas la bonificacion seria " + total);
        }

        int num = scan.nextInt();
        System.out.println(num);
    }
}
