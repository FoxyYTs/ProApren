package Taller1;

import java.util.Scanner;

public class pilaE2 {
    public static node2 top1 = null;
    public static node2 top2 = null;
    public static node2 top3 = null;


    public void push(int valor) {
        node2 nuevo = new node2(valor);
        nuevo.next = top;
        top = nuevo;
    }

    public node2 pop() {
        node2 temp = null;
        temp = top;
        top = top.next;
        return temp;
    }

    public boolean isEmpty() {
        node2 top = null;
        return top == null;
    }
    public void peak(node2 top){
        node2 pointer=top;
        while(pointer!=null){
            System.out.println(pointer.valor);
            pointer=pointer.next;
        }
    }
    static pilaE2 pila=new pilaE2();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        pilaE2 p1=new pilaE2();
        pilaE2 p2=new pilaE2();
        pilaE2 p3=new pilaE2();
        p1.push(1);
        p1.push(3);
        p1.push(5);
        node2 pointer=top1;
        while(pointer!=null){
            System.out.println(pointer.valor);
            pointer=pointer.next;
        }
        p3.push(p1.pop().valor);
        p2.push(p1.pop().valor);
        p2.push(p3.pop().valor);
        p3.push(p1.pop().valor);
        p1.push(p2.pop().valor);
        p3.push(p2.pop().valor);
        p3.push(p1.pop().valor);



        
    }
}
