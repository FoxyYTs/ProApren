package Repaso;
public class min {
    public static int sumar(Nodo head, int suma){
    if(head==null){
        return suma;
    }else{
        return sumar(head.next, suma+head.valor);
    }
    }
    public static void main(String[] args) {
        Linked L1=new Linked();
        L1.agregar(3);
        L1.agregar(4);
        L1.agregar(5);
        L1.mostrar();
        int total=sumar(L1.head, 0);
        System.out.println(total);
    }
}
