public class Main {

    public static int sumaListaLigada(Nodo cabeza) {
        return sumaListaLigadaRecursiva(cabeza, 0);
    }

    private static int sumaListaLigadaRecursiva(Nodo x, int sum) {
        if (x == null) {
            return sum;
        } else {
            sum += x.dato;
            return sumaListaLigadaRecursiva(x.siguiente, sum);
        }
    }

    public static void main(String[] args) {
        
        Suma Lista = new Suma();

        for (int i = 0; i <= 10; i++) {
            Lista.insertar(i);
        }

        int resultado = sumaListaLigada(Lista.cabeza);
        System.out.println("Suma de elementos de la lista: " + resultado);
    }
}