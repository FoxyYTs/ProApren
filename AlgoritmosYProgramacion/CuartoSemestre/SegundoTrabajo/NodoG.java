package AlgoritmosYProgramacion.CuartoSemestre.SegundoTrabajo;

public class NodoG {
    private boolean tag;
    private char dato;
    private NodoG sublist;
    private NodoG next;

    public NodoG(boolean tag){
        this.tag = tag;
        this.dato = ' ';
        this.sublist = null;
        this.next = null;
    }

    public boolean getTag(){
        return tag;
    }

    public char getDato(){
        return dato;
    }

    public NodoG getSublist(){
        return sublist;
    }

    public NodoG getNext(){
        return next;
    }

    public void setTag(boolean tag){
        this.tag = tag;
    }

    public void setDato(char dato){
        this.dato = dato;
    }

    public void setSublist(NodoG sublist){
        this.sublist = sublist;
    }

    public void setNext(NodoG next){
        this.next = next;
    }
}
