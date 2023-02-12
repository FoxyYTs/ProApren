import java.util.Scanner;

public class Nomina {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        String name;
        int h, vh, boni, subtotal, total, trabajador;

        System.out.println("Cuantos trabajadores va a evaluar ?");
        trabajador = leer.nextInt();
        System.out.println("Cuanto vale la bonificacion ?");
        boni = leer.nextInt();
        System.out.println("Cuanto Valen las horas ?");
        vh = leer.nextInt();

        for (int i = 0; i < trabajador; i++) {
            System.out.println("Como se llama el trabajador ?");
            name = leer.next();
            System.out.println("cuantas horas a trabajado ?");
            h = leer.nextInt();

            subtotal = h*vh;

            if (h > 48) {
                System.out.println(name + " a ganado una bonificacion de $" + boni);
            }else{
                System.out.println(name + " no a ganado ninguna bonificacion");
                boni = 0;
            }

            total = subtotal + boni;

            System.out.println("El trabajador " + name + " a Ganado $" + subtotal + " Por las horas trabajadas " + " Dando un total de $" + total);
        }
    }
}
