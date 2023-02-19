import java.util.Scanner;

public class MySecondProject {
        public static void main(String[]args){
            Scanner leer = new Scanner(System.in);
            int edad = 0;
            System.out.println("Que edad tienes ?");
            edad = leer.nextInt();
            if (edad >= 6 && edad <18){
                System.out.println("Bienvenido a la Miniteca");
            } else if (edad >= 18 && edad < 50) {
                System.out.println("Bienvenido a la Discoteca");
            } else if (edad >= 50) {
                System.out.println("Bienvenido a la Viejoteca");
            }else {
                System.out.println(edad + " no es una edad valida para entrar");
            }
        }
}