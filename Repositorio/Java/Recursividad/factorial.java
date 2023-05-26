package Repositorio.Java.Recursividad;

public class factorial {
    public static void main(String[] args) {
        int x = 4, y = 1;
        ciclo(x,y);
        //recursividad(x);
    }
    
    static void ciclo(int x, int y){
        int z;
        for(int i = 1; i <= x; i++){
            z = y;
            y = y*i;
            
            System.out.println(i + "X" + z + "=" + y);
        }
    }

    static void recursividad(int x, int y){
        
    }
}
