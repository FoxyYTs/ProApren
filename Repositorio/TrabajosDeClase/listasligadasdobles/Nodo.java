package Repositorio.TrabajosDeClase.listasligadasdobles;

public class Nodo {
    public int dato;
    public Nodo siguiente;
    public Nodo atras;
    
    public Nodo(int dato){
        this.dato = dato;
        this.siguiente = null;
        this.atras = null;
    }
}
