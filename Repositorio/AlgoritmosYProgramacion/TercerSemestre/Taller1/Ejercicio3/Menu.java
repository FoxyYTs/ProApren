package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio3;

import java.util.Scanner;

public class Menu {

    static Scanner leer = new Scanner(System.in);
    static Cola  cola = new Cola();

    public static void main(String[] args) {
        for (int i = 0; i <= 5; i++) {
            cola.ingreso();
        }
        int opcion;
        boolean continuar = true;
        while (continuar) {
            System.out.println("Bienvenido al Menu de atencion\n1) Ingresar\n2) Atender\n3) Eliminar\n4) Cerrar");
            opcion = Integer.parseInt(leer.nextLine());
            if (opcion == 1) {
                System.out.println("Ingresando nueva gente a la fila");
                leer.nextLine();
                cola.ingreso();
            } else if (opcion == 2){
                cola.atender();
            } else if (opcion == 3){
                System.out.println("Eliminaste a todos de la fila");
                leer.nextLine();
                cola.eliminar();
            } else if (opcion == 4){
                System.out.println("Cerrando menu");
                leer.nextLine();
                continuar = false;
            }
        }
        

    }
    
    
}
