package TrabajosDeClase.listasligadascirculares;

public class Main {
    public static void main(String[] args) {
        Listas listas = new Listas();

        for (int i = 1; i <= 10; i++) {
            listas.insertar("Hola" + i);
        }

        listas.mostrars();

        listas.mostrarsinv();

        listas.eliminar("Hola" + 10);

        listas.mostrars();

        listas.mostrarsinv();

        for (int i = 1; i <= 8; i++) {
            listas.eliminar("Hola" + i);

            listas.mostrars();

            listas.mostrarsinv();
        }
    }
}
