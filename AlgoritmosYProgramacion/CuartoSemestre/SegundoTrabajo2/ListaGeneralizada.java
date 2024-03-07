package AlgoritmosYProgramacion.CuartoSemestre.SegundoTrabajo2;

public class ListaGeneralizada {
    NodoLg head;
    NodoLg tail;
    int cant;

    public ListaGeneralizada() {
        head = null;
        tail = null;
        cant = 0;
    }

    public boolean Vacio() {
        return cant == 0;
    }

    public int cantidad(){
        return cant;
    }
}
