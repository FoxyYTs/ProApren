import java.util.Scanner;

public class MyThirdyProject {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numA = 0;

        System.out.println("Ingrese un numero");
        numA = leer.nextInt();
        System.out.println("==========");
        for (int i = 0;i < numA;i++){
            System.out.println(i);
        }
        for (int i = numA;i >= 0;i--){
            System.out.println(i);
        }
    }
}