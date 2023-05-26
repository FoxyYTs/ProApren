package Repositorio.TrabajosDeClase.listasligadascirculares;

public class Main {
    public static void main(String[] args) {
        Listas listas = new Listas();

        for (int i = 1; i <= 10; i++) {
            listas.insertar("Hola" + i);
        }
        
        listas.mostrar();

        listas.invmostrar();
    }
}
