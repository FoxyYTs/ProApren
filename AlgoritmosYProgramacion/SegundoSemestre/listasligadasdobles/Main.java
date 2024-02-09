package AlgoritmosYProgramacion.SegundoSemestre.listasligadasdobles;

public class Main {
    public static void main(String[] args) {
        Primero primero = new Primero();

        System.out.print("\033[H\033[2J");
        System.out.flush();

        for (int i = 1; i <= 10; i++) {
            primero.insertar("hola" + i);
        }

        System.out.println("Antes de eliminar");
        //primero.mostrar();
        

        primero.eliminar("hola7");

        primero.mostrar();
        System.out.println("========");
        primero.invmostrar();
    }
}
