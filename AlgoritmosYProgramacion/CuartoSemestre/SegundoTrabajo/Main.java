package AlgoritmosYProgramacion.CuartoSemestre.SegundoTrabajo;

import java.util.Scanner;
public class Main {
    static Scanner leer = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Ingresa una cadena");
        String cadena = leer.nextLine();
        if (!cadena.equals("")) {
            System.out.println(balanceador(cadena));
        }else{
            System.out.println("Esa cosa esta vacia");
        }
    }

    public static String balanceador(String cadena) {
        Pila list = new Pila();
        for (int i = 0; i < cadena.length(); i++) {
            if (cadena.charAt(i) == '(') {
                list.push(1);
            } else if (cadena.charAt(i) == ')'){
                list.pop();
            }
        }
        if (list.fill() != 0) {
            return "NO";
        } else {
            return "SI";
            
        }
    }
}
