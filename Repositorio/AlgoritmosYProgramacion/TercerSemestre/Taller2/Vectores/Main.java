package AlgoritmosYProgramacion.TercerSemestre.Taller2.Vectores;

import java.util.Vector;

public class Main {
    public static void main(String[] args) {
        Vector<Nodo> victor = new Vector<>();

        victor.addElement(new Nodo("Frank1", false, 100));
        victor.add(new Nodo("Frank2", true, 200));
        victor.addElement(new Nodo("Frank3", false, 300));
        victor.addElement(new Nodo("Frank4", false, 400));

        for (int index = 0; index < 4; index++) {
            System.out.println("Vector " + victor.get(index).dueño);
        }
    }
}
