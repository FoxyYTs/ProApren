package Repositorio.TrabajosDeClase.listasligadasdobles;

public class Main {
    public static void main(String[] args) {
        Primero primero = new Primero();

        for (int i = 1; i <= 10; i++) {
            primero.insertar("hola" + i);
        }

        primero.mostrar();

        primero.eliminar("hola1");

        primero.mostrar();
        System.out.println("========");
        primero.invmostrar();
    }
}
