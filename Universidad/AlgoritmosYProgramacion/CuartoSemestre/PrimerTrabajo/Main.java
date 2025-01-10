package AlgoritmosYProgramacion.CuartoSemestre.PrimerTrabajo;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        Lista list = new Lista();
        float[] notas = new float[5];
        int opcion = 0;
        boolean seguir = true;
        System.out.print("\033[H\033[2J");
        System.out.flush();
        System.out.println("Cargando los estudiantes del Archivo");
        leer.nextLine();
        list.fillFile();
        while (seguir) {
            list.ordenar();
            System.out.print("\033[H\033[2J");
            System.out.flush();
            System.out.println("MENU\n1) Ingresar estudiante\n2) Mostrar estudiante\n3) Borrar estudiante\n4) Cerrar");
            opcion = Integer.parseInt(leer.nextLine());
            if (opcion == 1) {
                System.out.println("Ingresando Estudiantes");
                Estudiante nuevo = new Estudiante();
                System.out.println("Ingresa el nombre");
                nuevo.setNombre(leer.nextLine());
                System.out.println("Ingresa el Apellido");
                nuevo.setApellido(leer.nextLine());
                for (int i = 0; i < 5; i++) {
                    System.out.println("Ingresa la nota "+(i+1));
                    notas[i] = Float.parseFloat(leer.nextLine());
                }
                nuevo.setNotas(notas);
                nuevo.setPromedio((notas[0]+notas[1]+notas[2]+notas[3]+notas[4])/5);
                list.insert(nuevo);
            } else if (opcion == 2) {
                System.out.print("\033[H\033[2J");
                System.out.println("que estudiantes quieres mostrar?\n1) Los mejores \n2) Todos");
                opcion = Integer.parseInt(leer.nextLine());
                if (opcion == 1) {
                    list.mostrarprom();
                } else if (opcion == 2){
                    list.mostrar();
                } else {
                    System.out.println("Opcion no valida");
                }
                leer.nextLine();
            } else if (opcion == 3){
                System.out.println("Borrando estudiantes con promedios menores a 2");
                list.borrar();
                leer.nextLine();
            } else if (opcion == 4){

                seguir = false;
            } else {
                System.out.println("Opcion no valida");
            }
        }
    }
}