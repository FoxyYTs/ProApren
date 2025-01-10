package AlgoritmosYProgramacion.CuartoSemestre.PrimerTrabajo;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Lista {
    private Estudiante head = null;
    int canStud = 0;

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
        canStud = studen.length;
        for (int x = 0; x < studen.length; x++) {
            String[] parts = studen[x].split(",");
            Estudiante nuevo = new Estudiante();
            for (int i = 6; i < parts.length; i+=6) {
                nuevo.setNombre(parts[i-6]);
                nuevo.setApellido(parts[i-5]);
                notas[0] = Float.parseFloat(parts[i-4]);
                notas[1] = Float.parseFloat(parts[i-3]);
                notas[2] = Float.parseFloat(parts[i-2]);
                notas[3] = Float.parseFloat(parts[i-1]);
                notas[4] = Float.parseFloat(parts[i]);
                nuevo.setNotas(notas);
                nuevo.setPromedio((notas[0]+notas[1]+notas[2]+notas[3]+notas[4])/5);
                insert(nuevo);
            }
        }
    }
    public void insert(Estudiante nuevo){
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

    public void borrar(){
        if (head == null){
            return;
        }
        Estudiante pointer = head;
        while (pointer != null) {
            if(pointer.next.getPromedio() < 2){
                pointer.next = null;
            }
            pointer = pointer.next;
        }
    }
    public void mostrar(){
        Estudiante pointer = head;
        while (pointer != null){
            System.out.println("Nombre: " + pointer.getNombre() + "\nApellido: " + pointer.getApellido() + "\nPromedio: " + pointer.getPromedio());
            pointer = pointer.next;
        }
    }
    public void mostrarprom(){
        Estudiante pointer = head;
        int estudiantes = 0;
        while (pointer != null && estudiantes < 3){
            System.out.println("Nombre: " + pointer.getNombre() + "\nApellido: " + pointer.getApellido() + "\nPromedio: " + pointer.getPromedio());
            pointer = pointer.next;
            estudiantes++;
        }
    }

    public void ordenar(){
        Estudiante pointer = head;
        Estudiante temp = null;
        int intentos = 0;
        while (pointer.next != null && intentos < canStud){
            if (pointer.next.getPromedio() > head.getPromedio()) {
                temp = pointer.next;
                pointer.next = pointer.next.next;
                temp.next = head;
                head = temp;
                intentos = 0;
                pointer = head;
            }
            pointer = pointer.next;
            intentos++;
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
