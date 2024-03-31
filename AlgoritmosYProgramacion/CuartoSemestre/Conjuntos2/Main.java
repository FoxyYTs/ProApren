package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos2;

public class Main {
    static Funciones funin = new Funciones();
    static Funciones fun = new Funciones();
    public static void main(String[] args) {
        Archivos in = new Archivos();

        System.out.println("Ingles");
        funin.mostrar();

        System.out.println("El Resto");
        fun.mostrar();

        if (Funciones.pertenece(fun.getHead(), "NombreyApellido3") == null) {
            System.out.println("No pertenece");
        }else{
            System.out.println("Pertenece");}

        fun.union(funin, fun);
        

        

        
    }
}
