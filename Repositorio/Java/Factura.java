import java.util.Scanner;

public class Factura {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Scanner cadena = new Scanner(System.in);
        int numb, i=0, nprduct, valor, total = 0, subtotal;
        String producto;
        System.out.println("Dijite la cantidad de productos a evaluar");
        numb = leer.nextInt();

        do{
            System.out.println("Ingrese el nombre del producto");
            producto = cadena.nextLine();

            System.out.println("Ingrese la cantidad del producto");
            nprduct = leer.nextInt();
            System.out.println("ingrese el valor de los productos");
            valor = leer.nextInt();

            subtotal = nprduct * valor;

            System.out.println("El valor de " + nprduct + " " + producto + " es " + subtotal);

            total += subtotal;
            i++;

        }while(i<numb);
        System.out.println("El valor final es " + total);


    }
}
