package AlgoritmosYProgramacion.CuartoSemestre.SegundoTrabajo;

public class colaG {
    NodoG head;
    int size;
    int cantSubList;

    public colaG(){
        head = null;
    }

    public void insert(boolean tag,char dato, char sublist){
        char ultimo;
        NodoG nuevo = new NodoG(tag);
        nuevo.setDato(dato);

        if (head == null){
            head = nuevo;
        } else {
            NodoG pointer = head;
            while (pointer.getNext() != null|| pointer.getDato() == ultimo){
                if (pointer.getSublist() != null && pointer.getDato() == ultimo) {
                    NodoG pointer2 = pointer.getSublist();
                    recorrer(pointer, ultimo)
                }
            }
        }
    }

    private static void recorrer(NodoG pointer, char dato){
    }
}
