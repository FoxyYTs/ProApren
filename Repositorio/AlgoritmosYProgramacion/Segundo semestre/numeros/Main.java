package TrabajosDeClase.numeros;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        
        int opcionA = 0,opcionB = 0;
        String valor = "";
        boolean x = true;

        System.out.print("\033[H\033[2J");
        System.out.flush();


        while (x) {
            
            System.out.print("Ingrese el numero que quiera convertir: ");
            valor = leer.nextLine();

            System.out.print("\033[H\033[2J");
            System.out.flush();

            System.out.println("En que base esta escrito este numero?\n1) Decimal\n2) Binario\n3) Octal\n4) Hexadecimal\n5) Cerrar Programa");
            opcionA = Integer.parseInt(leer.nextLine());
            
            switch (opcionA) {
                case 1:
                    System.out.println("El numero " + valor + " es en base Decimal");
                    opcionB = destino(opcionA, "D");
                    break;
    
                case 2:
                    System.out.println("El numero " + valor + " es en base Binario");
                    opcionB = destino(opcionA, "B");
                    break;
                
                case 3:
                    System.out.println("El numero " + valor + " es en base Octal");
                    opcionB = destino(opcionA, "O");
                    break;
                
                case 4:
                    System.out.println("El numero " + valor + " es en base Hexadecimal");
                    opcionB = destino(opcionA, "H");
                    break;

                case 5:
                    System.out.println("Cerrando Programa...");
                    x = false;
                    break;
            
                default:
                    System.out.println("Opcion no valida");
                    x = true;
                    break;
            }
            System.out.println("El resultado de la conversion es: " + elecF(opcionA, opcionB, valor));
        }

    }

    public static int destino(int a, String op1){
        Scanner leer = new Scanner(System.in);
        
        String bases[] = {"Decimal","Binario","Octal", "Hexadecimal"};
        System.out.println("A que base lo quieres convertir?\n1) Decimal\n2) Binario\n3) Octal\n4) Hexadecimal\n5) Cerrar Programa");
        int opcion = Integer.parseInt(leer.nextLine());
        switch (opcion) {
            case 1:
                System.out.println("Vas a convertir un numero de Base " + bases[a-1] + " a Base Decimal");
                return opcion;

            case 2:
                System.out.println("Vas a convertir un numero de Base " + bases[a-1] + " a Base Binario");
                return opcion;

            case 3:
                System.out.println("Vas a convertir un numero de Base " + bases[a-1] + " a Base Octal");
                return opcion;

            case 4:
                System.out.println("Vas a convertir un numero de Base " + bases[a-1] + " a Base Hexadecimal");
                return opcion;

            default:
                System.out.println("Opcion no valida");
                return 0;


        }
    }

    public static String elecF(int opcionA,int opcionB, String valor){
        Funciones conv = new Funciones();

        if (opcionA == 1 && opcionB == 2){
            return conv.DaB(valor);
        } else if (opcionA == 1 && opcionB == 3){
            return conv.DaO(valor);
        } else if (opcionA == 1 && opcionB == 4){
            return conv.DaH(valor);
        } else if (opcionA == 2 && opcionB == 1){
            return conv.BaD(valor);
        } else if (opcionA == 2 && opcionB == 3){
            return conv.BaO(valor);
        } else if (opcionA == 2 && opcionB == 4){
            return conv.BaH(valor);
        } else if (opcionA == 3 && opcionB == 1){
            return conv.OaD(valor);
        } else if (opcionA == 3 && opcionB == 2){
            return conv.OaB(valor);
        } else if (opcionA == 3 && opcionB == 4){
            return conv.OaH(valor);
        } else if (opcionA == 4 && opcionB == 1){
            return conv.HaD(valor);
        } else if (opcionA == 4 && opcionB == 2){
            return conv.HaB(valor);
        } else if (opcionA == 4 && opcionB == 3){
            return conv.HaO(valor);
        }else {
            System.out.println("Opcion no valida");
        }
        return "A";
    }
}
