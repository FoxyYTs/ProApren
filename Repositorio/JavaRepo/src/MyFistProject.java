import java.util.Scanner;
public class MyFistProject {
    public static void main(String[]args){
        Scanner leer = new Scanner(System.in);
        int numTo = 0,numCan = 0;
        System.out.println("Cuantos numeros va a sumar ?");
        numCan = leer.nextInt();
        for (int i = 0; i < numCan; i++){
            System.out.println("Ingrese un numero");
            numTo += leer.nextInt();
            System.out.println("llevas un total de: " + numTo);
        }
        System.out.println("el total de todos los numeros es: " + numTo);
    }
}
