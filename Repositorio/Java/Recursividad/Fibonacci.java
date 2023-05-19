package Repositorio.Java.Recursividad;

public class Fibonacci {
    public static void main(String[] args) {
        System.out.println("Ciclos");
        ciclo(10);

        System.out.println("Recursivo");
        recursivo(1,0,10);
    }
    public static void ciclo(int a){
        int aN = 1,bN = 0,cN;
        for (int i = 0; i < a; i++) {
            cN = aN + bN;
            System.out.println(aN + "+" + bN + "=" + cN);
            bN = aN;
            aN = cN;
        }
    }
    
    public static void recursivo(int cN,int bN,int aN) {
        if (aN > 0) {
            int dN = cN + bN;
            System.out.println(cN + "+" + bN + "=" + dN);
            recursivo(dN, cN, aN - 1);
        }
    }
}
