package TrabajosDeClase.listas;

import java.util.*;
public class eje1 {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        ListasLigadas lista = new ListasLigadas();

        for (int i = 1; i <= 5; i++) {
            lista.insertar(i);
        }

        lista.mostrar();
    }
}