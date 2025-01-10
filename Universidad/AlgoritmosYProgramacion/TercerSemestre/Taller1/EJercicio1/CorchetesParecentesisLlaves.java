package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio1;

public class CorchetesParecentesisLlaves {
    static Funcion fun = new Funcion();
    public static void main(String[] args) {
        String cadena = "({[Hola buenas tardes])}";

        if (fun.estaBalanceado(cadena)) {
            System.out.println("La entrada está balanceada.");
        } else {
            System.out.println("La entrada no está balanceada.");
        }
    }

}
