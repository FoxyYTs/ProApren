package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio2;

public class TorreHanoi {
    Pila pila = new Pila();

    public void juego(){
        for (int i = 1; i <= 3; i++) {
            pila.push1(i);
        }
    }
}
