package Hilos;

public class Hilosinterfaz {

    public static void main(String[] args) {

        hiloVentan ventana = new hiloVentan();

        hilo hiloReloj = new hilo(ventana);
        hiloAbecedario hiloABC = new hiloAbecedario(ventana);

        hiloReloj.start();
        hiloABC.start();
    }
}