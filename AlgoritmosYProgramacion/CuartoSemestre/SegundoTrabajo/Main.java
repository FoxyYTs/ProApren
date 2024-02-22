package AlgoritmosYProgramacion.CuartoSemestre.SegundoTrabajo;

import java.util.Scanner;
public class Main {
    static Scanner leer = new Scanner(System.in);
    public static void main(String[] args) {
        Balanceador bal = new Balanceador();
        System.out.println("Ingresa una cadena");
        String cadena = leer.nextLine();
        if (!cadena.equals("")) {
            System.out.println(bal.balanceador(cadena));
        }else{
            System.out.println("Esa cosa esta vacia");
        }
    }
}
