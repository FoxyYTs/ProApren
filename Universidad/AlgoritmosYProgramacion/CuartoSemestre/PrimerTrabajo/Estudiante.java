package AlgoritmosYProgramacion.CuartoSemestre.PrimerTrabajo;

public class Estudiante {
    private String nombre;
    private String Apellido;
    private float[] notas = {0,0,0,0,0};
    private float promedio;
    Estudiante next;

    public Estudiante(){
        this.nombre = "asd";
        this.Apellido = null;
        this.notas = null;
        this.promedio = 0;
    }



    public String getNombre(){
        return nombre;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public String getApellido(){
        return Apellido;
    }

    public void setApellido(String Apellido){
        this.Apellido = Apellido;
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
