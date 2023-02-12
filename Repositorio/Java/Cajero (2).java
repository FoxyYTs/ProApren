import java.util.Scanner;

public class Cajero {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double id;
        int op, saldo, canti,consignacion, canre=0, cancon = 0;
        String i = "Encendido", ops = "",a;
        while (i != "Apagar") {
            saldo = 1000000;
            System.out.println("===========================");
            System.out.println("Cual es su numero de cuenta?");
            id = leer.nextDouble();
            if (id == 1.987) {
                System.out.println("Usted a entrado en el modo administrador");
                System.out.println("Si quieres mirar los registros de hoy escribe 'Registros'\nSi quiere Apagar escribe 'Apagar'");
                a = leer.next();

                switch (a) {
                    case "Registros":
                        System.out.println("La Cantidad de consignaciones realizadas son: " + cancon + "\nLa Cantidad de retiros son: " + canre);    
                        break;
                    case "Apagar":
                        i = "Apagar";
                        break;
                    default:
                        System.out.println("Opcion no valida");
                        break;
                }
            }else{
                System.out.println("Bienvenido señor usuario, que desea hacer ?");
                System.out.println("Su saldo actual es de: " + saldo + "\n1 -> realizar un retiro\n2 -> realizar consignacion");
                op = leer.nextInt();
                switch (op) {
                    case 1:
                        System.out.println("Cual es la cantidad que desea retirar?");
                        canti = leer.nextInt();
                        System.out.println("Seguro que quiere retirar $" + canti + ", La cantidad que quedara en su cuenta seran de $" + (saldo-canti) + "\nsi/no");
                        ops = leer.next();
                        switch (ops) {
                            case "si":
                                System.out.println("El retiro fue exitoso");
                                canre++;
                                break;
                            case "no":
                                System.out.println("El Retiro fue cancelado");
                                break;
                            default:
                                System.out.println("Opcion no valida");
                                break;
                        }
                        break;
                    case 2:
                        System.out.println("A que numero de cuenta desea hacer la consignacion?");
                        consignacion = leer.nextInt();
                        System.out.println("Cuanto va a Consignar ?");
                        canti = leer.nextInt();
                        System.out.println("Seguro que quiere realizar una consignacion a la cuenta " + consignacion + " Por la cantidad de $" + canti+ " ?\nsi/no");
                        ops = leer.next();
                        switch (ops) {
                            case "si":
                                System.out.println("Se a Consignado $" + canti + " a la cuenta " + consignacion + " Con Exito");
                                cancon++;
                                break;
                            case "no":
                                System.out.println("Transaccion Cancelada");
                                break;
                            default:
                                System.out.println("Opcion no valida");
                                break;
                        }
                        break;            
                    default:
                        System.out.println("No a elegido una opcion valida");
                        break;
                }
            }
        }
        System.out.println("Fin programa");
    }
}