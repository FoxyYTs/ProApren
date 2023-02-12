import java.util.Scanner;
public class Snakify {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int a = leer.nextInt();
        System.out.println("The next number for the number "+ (a) + " is " + (a+1) +".");
        System.out.println("The previous number for the number "+(a)+" is " + (a-1) + ".");
    }
}

