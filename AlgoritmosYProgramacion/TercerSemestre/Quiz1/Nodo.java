package AlgoritmosYProgramacion.TercerSemestre.Quiz1;

public class Nodo {
    private Puesto TOP,A,B,C;

    public Nodo(Puesto TOP,Puesto A, Puesto B, Puesto C){
        this.TOP=TOP;
        this.A=A;
        this.B=B;
        this.C=C;
    }

    public Puesto getTOP() {
        return TOP;
    }

    public void setTOP(Puesto tOP) {
        TOP = tOP;
    }

    public Puesto getA() {
        return A;
    }

    public void setA(Puesto a) {
        A = a;
    }

    public Puesto getB() {
        return B;
    }

    public void setB(Puesto b) {
        B = b;
    }

    public Puesto getC() {
        return C;
    }

    public void setC(Puesto c) {
        C = c;
    }

    
}
