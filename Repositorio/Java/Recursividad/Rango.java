package Repositorio.Java.Recursividad;

public class Rango {
    public static void main(String[] args) {
        int x = 30, y = 40;
        System.out.println("Ciclos");
        ciclo(x,y);
        System.out.println("Recursividad");
        recursivo(x,y);
    }
    static void ciclo(int inicio, int fin){
        if(inicio > fin){
            for (int i = inicio; i >= fin ; i--) {
                System.out.println("Numero: " + i);
            }
        }else{
            for (int i = inicio; i <= fin ; i++) {
                System.out.println("Numero: " + i);
            }
        }
    }

    static void recursivo(int inicio, int fin){
        if(fin > inicio){
            recursivo(inicio, fin-1);
            System.out.println("Numero: " + fin);
        }else if(inicio > fin){
            recursivo(inicio, fin+1);
            System.out.println("Numero: " + fin);
        }else if(inicio == fin){
            System.out.println("Numero: " + fin);
        }
    }
}
