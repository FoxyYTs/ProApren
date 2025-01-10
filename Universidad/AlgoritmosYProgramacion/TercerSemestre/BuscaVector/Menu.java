package AlgoritmosYProgramacion.TercerSemestre.BuscaVector;

import java.util.Scanner;
import java.util.Vector;

public class Menu {

    public static void main(String[] args) {

        Vector cuentas = new Vector(5);
        cuentas.addElement("1001");
        cuentas.addElement("1002");
        cuentas.addElement("1003");
        cuentas.addElement("1004");
        cuentas.addElement("1005");

        Scanner leer = new Scanner(System.in);

        int opcion = 0;

        while (opcion != 5) {
            leer.nextLine();
            System.out.print("\033[H\033[2J");
            System.out.flush();

            System.out.println("Ingrese su numero de cuenta");


            System.out.print("Menú de Operaciones:\n1) Consultar Saldo\n2) Retiro\n3) Consignacion\n4) Ultima Operacion\n5) Salir\nIngrese su opción: ");
            opcion = leer.nextInt();

            switch (opcion) {
                case 1:

                    break;
                case 2:
                    break;
                case 3:
                    break;
                case 4:
                    break;
                case 5:
                    break;
                default:
                    break;
            }
        }
    }
}
