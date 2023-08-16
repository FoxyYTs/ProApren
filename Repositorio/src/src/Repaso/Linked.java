package Repaso;
public class Linked {
    public Nodo head;
    public void agregar(int num){
        Nodo temp=new Nodo(num);
        if(head==null){
           head=temp; 
        }else{
            Nodo pointer=head;
            while(pointer.next!=null){
                pointer=pointer.next;
            }pointer.next=temp;
        }
    }
    public void mostrar(){
        if(head==null){
            System.out.println("La lista está vacía");
        }else{
            Nodo pointer=head;
            while(pointer!=null){
                System.out.println(pointer.valor);
                pointer=pointer.next;
            }
        }
    }
}
