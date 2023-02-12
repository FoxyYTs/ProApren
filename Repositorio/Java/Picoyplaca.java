import java.util.Scanner;

public class Picoyplaca {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        String dia;
        int placa;
        System.out.println("Dijite el dia que quiere consultar");
        dia = leer.next();
        System.out.println("Dijite el numero de placa que quiere consultar");
        placa = leer.nextInt();
        switch (dia) {
            case "Lunes":
                if (placa == 6 || placa ==3) {
                    System.out.println("Su vehiculo no puede circular hoy");
                    break;
                } else {
                    System.out.println("El dia "+dia+" los vehiculos no pueden circulas los vehiculos que comiences por 6 o 3");
                    break;
                }
            case "Martes":
                if (placa == 9 || placa ==8) {
                    System.out.println("Su vehiculo no puede circular hoy");
                    break;
                } else {
                    System.out.println("El dia "+dia+" los vehiculos no pueden circulas los vehiculos que comiences por 9 o 8");
                    break;
                }
            case "Miercoles":
                if (placa == 4 || placa ==5) {
                    System.out.println("Su vehiculo no puede circular hoy");
                    break;
                } else {
                    System.out.println("El dia "+dia+" los vehiculos no pueden circulas los vehiculos que comiences por 4 o 5");
                    break;
                }
            case "Jueves":
                if (placa == 7 || placa ==1) {
                    System.out.println("Su vehiculo no puede circular hoy");
                    break;
                } else {
                    System.out.println("El dia "+dia+" los vehiculos no pueden circulas los vehiculos que comiences por 7 o 1");
                    break;
                }
            case "Viernes":
                if (placa == 2 || placa ==0) {
                    System.out.println("Su vehiculo no puede circular hoy");
                    break;
                } else {
                    System.out.println("El dia "+dia+" los vehiculos no pueden circulas los vehiculos que comiences por 2 o 0");
                    break;
                }
            case "Sabado","Domingo":
                System.out.println("Los Sabados y Domingos no hay restricciones");
                break;
            default:
                System.out.println("Lo que usted a ingresado no es valido");
                break;
        }
    }
}
