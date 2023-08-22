package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio3;

import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);
        Cola cola = new Cola();

        int opcion;
        boolean continuar = true;

        while (continuar) {
            leer.nextLine();
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.print("Menú de Operaciones:\n1) Adicionar persona a la cola\n2) Atender persona de la cola\n3) Cambiar prioridad de atención\n4) Eliminar cola\n5) Salir\nIngrese su opción: ");
            opcion = leer.nextInt();

            if (opcion == 1){
                int edad = (int) (Math.floor(Math.random()*(60-18+1)+18));
                System.out.println("Edad del cliente: " + edad);

                boolean embarazada = false;

                if((int)(Math.random()*5) == 1){
                    System.out.println("La Clienta esta Embarazada");
                    embarazada = true;
                }

                System.out.print("Ingrese nombre: ");
                String nombre = leer.next();

                cola.encolar(nombre, edad, embarazada);
                leer.nextLine();
            } else if (opcion == 2){
                Nodo atendida = cola.desencolar();
                if (atendida != null) {
                    System.out.println("Persona atendida: " + atendida.nombre);
                } else {
                    System.out.println("La cola está vacía.");
                }
                leer.nextLine();
            } else if (opcion == 3){
                System.out.print("Ingrese el nombre de la persona para cambiar prioridad: ");
                cola.cambiarPrioridad(leer.next());
                leer.nextLine();
            } else if (opcion == 4){
                cola.eliminarCola();
                System.out.println("Cola eliminada.");
                leer.nextLine();
            } else if (opcion == 5){
                System.out.println("Saliendo...");
                continuar = false;
                leer.nextLine();
            } else {
                System.out.println("Opción inválida."); 
                leer.nextLine();
            }

            System.out.println("Cola actual: ");
            cola.print();
        }
    }
}
