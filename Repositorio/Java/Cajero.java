import java.util.Scanner;

public class Cajero {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double id;
        String a = "Encendido";
        while (a = "Apagado") {
            System.out.println("Cual es su numero de cuenta?");
            id = leer.nextDouble();
            if (id == 1.987) {
                System.out.println("Usted a entrado en el modo administrador");
                System.out.println("Si quiere Apagar dijite 'Apagar' ");
                i = leer.nextLine();
            }else{
                System.out.println("Bienvenido señor usuario, que desea hacer ?");
                System.out.println("Su saldo actual es de: " + saldo + "1 -> realizar un retiro\n2 -> realizar consignacion");
                op = leer.nextInt();
                switch (op) {
                    case 1:
                        System.out.println("Cual es la cantidad que desea retirar?");
                        break;
                    case 2:
                        System.out.println("A que numero de cuenta desea hacer la consignacion?");
                        break;
                    default:
                        System.out.println("No a elegido una opcion valida");
                        break;
                }
            }
        }

    }
}
