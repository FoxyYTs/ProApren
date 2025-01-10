package Java;

import java.util.Scanner;
public class main {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        if (esPrimo(leer.nextInt())) {
            System.out.println("Es primo");
        } else {
            System.out.println("No es primo");
            
        }
    }

    static boolean esPrimo(int n) {
        for(int i=2;i<n;i++) {
            if(n%i==0)
                return false;
        }
        return true;
    }
}
