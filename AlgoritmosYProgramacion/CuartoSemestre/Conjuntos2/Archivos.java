package AlgoritmosYProgramacion.CuartoSemestre.Conjuntos2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Archivos {

    public Archivos(){
        inicio();
    }

    public void inicio(){
        llenarArchivo();
        fillFile();
    }
    
    public void llenarArchivo(){
        String[] studen = leerArchivo().split("-");
        float[] notas = new float[3];
        for (int x = 0; x < studen.length; x++) {
            String[] parts = studen[x].split(",");
            Nodo nuevo = new Nodo();
            for (int i = 3; i < parts.length; i+=3) {
                nuevo.setName(parts[i-3]);
                notas[0] = Float.parseFloat(parts[i-2]);
                notas[1] = Float.parseFloat(parts[i-1]);
                notas[2] = Float.parseFloat(parts[i]);
                nuevo.setNota(notas);
                Main.fun.insert(nuevo);
            }
        }
    }
    
    public String leerArchivo(){
        try {
            BufferedReader input = new BufferedReader(new FileReader("./AlgoritmosYProgramacion/CuartoSemestre/Conjuntos2/EstuTodas.txt"));
            String datos = input.readLine();
            input.close();
            return datos;
        } catch (IOException e) {
            return "No se pudo leer el archivo";
        }
    }

    public void fillFile(){
        String[] studen = readFile().split("-");
        float[] notas = new float[1];
        for (int x = 0; x < studen.length; x++) {
            String[] parts = studen[x].split(",");
            Nodo nuevo = new Nodo();
            for (int i = 3; i < parts.length; i+=3) {
                nuevo.setName(parts[i-3]);
                notas[0] = Float.parseFloat(parts[i]);
                nuevo.setNota(notas);
                Main.funin.insert(nuevo);
            }
        }
    }
    
    public String readFile(){
        try {
            BufferedReader input = new BufferedReader(new FileReader("./AlgoritmosYProgramacion/CuartoSemestre/Conjuntos2/Estuingles.txt"));
            String datos = input.readLine();
            input.close();
            return datos;
        } catch (IOException e) {
            return "No se pudo leer el archivo";
        }
    }
}
