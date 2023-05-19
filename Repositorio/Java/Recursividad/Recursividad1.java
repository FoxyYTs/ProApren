package Repositorio.Java.Recursividad;

public class Recursividad1 {
    public static void main(String[] args) {
        System.out.println("Ciclos");
        ciclo(10);
        System.out.println("Recursividad");
        recursivo(10);
    }

    public static void ciclo(int i){
        for (int j = 1; j <= i; j++) {
            System.out.println("Numero: " + j);
        }
    }

    public static void recursivo(int i){
        if(i > 0){
            recursivo(i-1);
            System.out.println("Numero: " + i);
        }
    }
}
