package AlgoritmosYProgramacion.TercerSemestre.Taller1.EJercicio1;

public class CorchetesParecentesisLlaves {
    static funciones fun = new funciones();
    public static void main(String[] args) {
        String cadena = "{([Hola buenas tardes]})";

        for (int n = 0; n < cadena.length(); n++) {
            fun.insertar(String.valueOf(cadena.charAt(n))); 
        }

        fun.mostrar();
        System.out.println(fun.igualador());;
    }

}
