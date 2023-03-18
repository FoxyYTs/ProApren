package Repositorio.TrabajosDeClase.listas;

public class Nodo {
    public String nombre;
    public String genero;
    public int edad;
    
    public Nodo(String nombre,String genero, int edad){
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
    }
    public Nodo next = null;

    /*public void vetor(){
        Nodo[] vectorNodos = new Nodo[10];
        for(int i = 0; i<9; i++){
        vectorNodos[i] = new Nodo();
        }
    }*/
}
