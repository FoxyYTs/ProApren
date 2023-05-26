package Repositorio.Java.Recursividad;

public class invertir {
    public static void main(String[] args) {
        int num = 123456;
        int numInvertidoC = ciclo(num);
        int numInvertidoR = recursividad(num,0);
        System.out.println("Numero Original: " + num);
        System.out.println("El número invertido por Ciclo: " + numInvertidoC);
        System.out.println("El número invertido por Recursividad: " + numInvertidoR);

    }
    
    public static int ciclo(int num) {
        int numInvertido = 0;
        
        while (num > 0) {
            numInvertido = numInvertido * 10 + num % 10;
            num /= 10;
        }
        
        return numInvertido;
    }

    public static int recursividad(int num,int numInvertido){
        if (num == 0) {
            return numInvertido; 
        }
        int ultimoDigito = num % 10;
        numInvertido = numInvertido * 10 + ultimoDigito;
    
        return recursividad(num / 10, numInvertido);
    }
    
}
