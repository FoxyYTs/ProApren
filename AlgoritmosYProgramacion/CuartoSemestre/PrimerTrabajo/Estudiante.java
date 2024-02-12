package AlgoritmosYProgramacion.CuartoSemestre.PrimerTrabajo;

public class Estudiante {
    private String nombre;
    private float[] notas = new float[5];
    private float promedio;
    Estudiante next;

    public Estudiante(){}
    public Estudiante(String nombre, float[] notas, float promedio, Estudiante next){
        this.nombre = null;
        this.notas = null;
        this.promedio = (Float) null;
        this.next = null;
    }


    public String getNombre(){
        return nombre;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public float[] getNotas(){
        return notas;
    }

    public void setNotas(float[] notas){
        this.notas = notas;
    }

    public float getPromedio(){
        return promedio;
    }

    public void setPromedio(float promedio){
        this.promedio = promedio;
    }
}
