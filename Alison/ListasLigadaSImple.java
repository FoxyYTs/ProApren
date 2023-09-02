package Alison;

public class ListasLigadaSImple {
    Nodo head = null;
    Nodo head2=null;

    public void eliminar(Nodo direccion){
         Nodo pointer=head;
         while(pointer != null){
            if(pointer.next==direccion){
                pointer.next = pointer.next.next;
            }
            pointer=pointer.next;
         }

    }

    public void listas(){
        Nodo pointer=head;
        Nodo poiterNodo=head2;
        while(pointer.next != null){
            pointer = pointer.next;
        }
        pointer.next = head2;
    }
        
    public void insertar(int valor){
        Nodo nuevo = new Nodo(valor);
        if (head == null){
            head = nuevo;
        }else{
            Nodo pointer = head;
            while (pointer.next != null){
                pointer = pointer.next;
            }
            pointer.next = nuevo;
        }
    }


}
