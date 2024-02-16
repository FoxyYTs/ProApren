package AlgoritmosYProgramacion.CuartoSemestre.PrimerTrabajo;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Lista {
    private Estudiante head;

    public Lista(){
    }

    public void setHead(Estudiante head) {
        this.head = head;
    }

    public Estudiante getHead() {
        return head;
    }

    public void fillFile(){
        String[] studen = readFile().split("-");
        float[] notas = new float[5];
        for (int x = 0; x < studen.length; x++) {
            String[] parts = studen[x].split(",");
            Estudiante nuevo = new Estudiante();
            for (int i = 6; i < parts.length; i++) {
                nuevo.setNombre(parts[i-6]);
                nuevo.setApellido(parts[i-5]);
                notas[0] = Float.parseFloat(parts[i-4]);
                notas[1] = Float.parseFloat(parts[i-3]);
                notas[2] = Float.parseFloat(parts[i-2]);
                notas[3] = Float.parseFloat(parts[i-1]);
                notas[4] = Float.parseFloat(parts[i]);
                nuevo.setNotas(notas);
    
                System.out.println(nuevo.getNombre());
                System.out.println(nuevo.getApellido());
                for (int j = 0; j < 5; j++) {
                    System.out.println(nuevo.getNotas()[j]);
                }

            }
            if (head == null) {
                head = nuevo;
            } else {
                Estudiante pointer = head;
                while(pointer.next != null){
                    pointer = pointer.next;
                }
                pointer.next = nuevo;
            }
        }
    }

    public String readFile(){
        try {
            BufferedReader input = new BufferedReader(new FileReader("./AlgoritmosYProgramacion/CuartoSemestre/PrimerTrabajo/Estudiantes.txt"));
            String datos = input.readLine();
            input.close();
            return datos;
        } catch (IOException e) {
            return "No se pudo leer el archivo";
        }
    }
}
