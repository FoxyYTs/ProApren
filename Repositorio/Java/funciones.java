package Repositorio.Java;

public class funciones {

    public static void main(String[] args) {
        int y = 3;
        System.out.println("Circulo: " + areaCirculo(y) + "\nEsfera: " + areaEsfera(y) + "\nVolumen Esfera: " + volumenEsfera(y));
    }
    /**
     * Calcula el Area de un Circulo
     * @param r
     * @return Pi*r,2
     */
    public static double areaCirculo(double r){
        return Math.PI * Math.pow(r,2);
    }
    /**
     * Calcula el Area de una Esfera
     * @param r
     * @return
     */
    public static double areaEsfera(double r) {
        return 4 * Math.PI * Math.pow(r,2); 
    }
    /**
     * Calcula el volumen de una esfera
     * @param r
     * @return
     */
    public static double volumenEsfera(double r){
        return (4/3) * Math.PI * Math.pow(r,3);
    }
}