package Repositorio.TrabajosDeClase.TallerMadrid;

public class Complejo2 {
    private double real;
    private double img;

    public Complejo2() {
   
    }

    public Complejo2(double real, double img){
        this.real = real;
        this.img = img;
    }

    public double getImg(){
        return img;
    }

    public void setImg(){
        this.img = img;
    }

    public double getReal(){
        return real;
    }

    public void setReal(){
        this.real = real;
    }

    public Complejo2 sumar(Complejo2 c){
        Complejo2 a = new Complejo2();
        a.real = real + c.real;
        a.img = img + c.img;
        return c;
    }

    public Complejo2 restar(Complejo2 c){
        Complejo2 a = new Complejo2();
        a.real = real - c.real;
        a.img = img - c.img;
        return a;
    }

    public Complejo2 multiplicar(Complejo2 c){
        Complejo2 a = new Complejo2();
        a.real = real * c.real;
        a.img = img * c.img;
        return a;
    }

    public Complejo2 dividir(Complejo2 c){
        Complejo2 a = new Complejo2();
        a.real = real / c.real;
        a.img = img / c.img;
        return a;
    }
    
}
