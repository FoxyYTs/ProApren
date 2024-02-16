package AlgoritmosYProgramacion.CuartoSemestre.PrimerTrabajo;

import java.io.*;

public class Main {
    private static Estudiante estudiante;

    public static void main(String[] args) {
        String[] studen = readTB().split("-");
        float[] notas = new float[5];
        for (int x = 0; x < studen.length; x++) {
            String[] parts = studen[x].split(",");
            for (int i = 6; i < parts.length; i++) {
                Estudiante nuevo = new Estudiante();
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
            if (cabeza == null) {
                cabeza = nuevo;
            } else {
                Nodo actual = cabeza;
                while(actual.siguiente != null){
                    actual = actual.siguiente;
                }
                actual.siguiente = nuevo;
            }
        }

        
        
    }
    private static String readFile() {
        try {
            BufferedReader input = new BufferedReader(new FileReader("./AlgoritmosYProgramacion/CuartoSemestre/PrimerTrabajo/Estudiantes.txt"));
            String tbMaxScore = input.readLine();
            input.close();
            return tbMaxScore;
        } catch (IOException e) {
            return null;
        } catch (NumberFormatException e) {
            return null;
        }
    }

    private static void writeTB(int tbScore) {
        try {
            File UIFile = new File("./AlgoritmosYProgramacion/CuartoSemestre/PrimerTrabajo/Tetris.txt   ");
            if (!UIFile.exists()) {
                UIFile.createNewFile();
            }
            FileWriter filewriter = new FileWriter(UIFile.getAbsoluteFile());
            BufferedWriter outputStream = new BufferedWriter(filewriter);
            outputStream.write(String.valueOf(tbScore));
            outputStream.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}