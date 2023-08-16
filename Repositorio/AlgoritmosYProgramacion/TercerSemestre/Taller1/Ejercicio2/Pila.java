package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio2;

public class Pila {
    static Nodo top1;
    static Nodo top2;
    static Nodo top3;
    static String pPartida, destino;
    static int ficha;
    
    public Pila() {
        top1 = null;
        top2 = null;
        top3 = null;
    }

    public static void llenado(){
        for (int i = 3; i >= 1; i--) {
            push1(i);
        }
    }
        
    public static void push1(int elemento) {
        Nodo nuevoNodo = new Nodo(elemento);
        if (top1 == null) {
            top1 = nuevoNodo;

        } else {
            top1.back = nuevoNodo;
            nuevoNodo.next = top1;
            top1 = top1.back;
        }
        destino = "Torre 1";
    }
        
    public static int pop1() {
        if (top1 == null) {
            return '0' ;
        }
        int caracter = top1.elemento;
        top1 = top1.next;
        return caracter;
        pPartida = ""
    }

    public static void push2(int elemento) {
        Nodo nuevoNodo = new Nodo(elemento);
        if (top2 == null) {
            top2 = nuevoNodo;
        } else {
            top2.back = nuevoNodo;
            nuevoNodo.next = top2;
            top2 = top2.back;
        }
        destino = "Torre 2";
    }
        
    public static int pop2() {
        if (top2 == null) {
            return '0' ;
        }
        int caracter = top2.elemento;
        top2 = top2.next;
        return caracter;
    }

    public static void push3(int elemento) {
        Nodo nuevoNodo = new Nodo(elemento);
        if (top3 == null) {
            top3 = nuevoNodo;
        } else {
            top3.back = nuevoNodo;
            nuevoNodo.next = top3;
            top3 = top3.back;
        }
        destino = "Torre 3";
    }
        
    public static int pop3() {
        if (top3 == null) {
            return '0' ;
        }
        int caracter = top3.elemento;
        top3 = top3.next;
        return caracter;
    }

    public static void print() {
        System.out.println("La Ficha " + ficha + " salio de " + pPartida + " y se puso en " + destino);
    }

    public void juego(){
        push3(pop1());
        push2(pop1());
        push2(pop3());
        push3(pop1());
        push1(pop2());
        push3(pop2());
        push3(pop1());
    }

}
