package Repositorio.TrabajosDeClase.Pilas;

public class Main {
    public static void main(String[] args) {
        Pilas pilas = new Pilas();
        pilasBasicas(pilas);

        
        
    }

    public static void pilasBasicas(Pilas pilas){
        for (int i = 1; i <= 6; i=i+2) {
            pilas.insertarA(i);
        }

        for (int i = 2; i <= 6; i=i+2) {
            pilas.insertarB(i);
        }

        pilas.mostrarA();

        pilas.mostrarB();
    }
}
