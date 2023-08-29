package AlgoritmosYProgramacion.TercerSemestre.Quiz1;

public class Funciones {
    Nodo[] Sala1 = new Nodo[7];
    //A2-3-4 Movilidad reducida
    //B0-6 Descuento 10%
    //C0-6 Descuento 10% C2-3-4 Sonido y Vibrador 
    Nodo[] Sala2 = new Nodo[7];
    //A0-6 Descuento 10% A2-3-4 Movilidad reducida
    //B2-3-4 Sonido y Vibrador
    //C0-6 Descuento 10% C1-2-3-4-5 Sonido y Vibrador

    public double calcuprecio1 (String tipo){
        if (tipo.equals("Movilidad Reducida")) {
            return 12500-12500*0.15;
        } else if (tipo.equals("Descuento 10%")) {
            return 12500-12500*0.1;
        } else if (tipo.equals("Sonido y Vibracion")){
            return 12500+12500*0.25;
        } else {
            return 12500;
        }
    }

    public double calcuprecio2 (String tipo){
        System.out.println("Al valor de la boleta se le agregara un valos extra de 2800 para las gafas 3D.");
        if (tipo.equals("Movilidad Reducida")) {
            return 14500-14500*0.15+2800;
        } else if (tipo.equals("Descuento 10%")) {
            return 14500-14500*0.1+2800;
        } else if (tipo.equals("Sonido y Vibracion")){
            return 14500+14500*0.25+2800;
        } else {
            return 14500+2800;
        }
    }

    public String convSala1(String asiento){
        if (asiento.equals("A2") || asiento.equals("A3") || asiento.equals("A4")){
            return "Movilidad Reducida";
        } else if (asiento.equals("B0") || asiento.equals("B6") ||asiento.equals("C0") || asiento.equals("C6")){
            return "Descuento 10%";
        } else if (asiento.equals("C2") || asiento.equals("C3") ||asiento.equals("C4")){
            return "Sonido y Vibracion";
        } else {
            return "General";
        }
    }

    public String convSala2(String asiento){
        if (asiento.equals("A2") || asiento.equals("A3") || asiento.equals("A4")){
            return "Movilidad Reducida";
        } else if (asiento.equals("A0") || asiento.equals("A6")){
            return "Descuento 10%";
        } else if (asiento.equals("B2") || asiento.equals("B3") ||asiento.equals("B4") || asiento.equals("C1") || asiento.equals("C2") || asiento.equals("C3") || asiento.equals("C4")){
            return "Sonido y Vibracion";
        } else {
            return "General";
        }
    }

    public void reseva(int peli, String asiento, String nombre){
        if (peli == 1) {
            for (int i = 0; i < Integer.parseInt(asiento.substring(1)); i++) {
                if (asiento.substring(0).equals("A")){
                    Sala1[i] = new Nodo(new Puesto(nombre, convSala1(asiento), true, calcuprecio1(convSala1(asiento))),Sala1[i].B,Sala1[i].C);
                } else if (asiento.substring(0).equals("B")) {
                    Sala1[i] = new Nodo(Sala1[i].A, new Puesto(nombre, convSala1(asiento), true, calcuprecio1(convSala1(asiento))), Sala1[i].C);
                } else if (asiento.substring(0).equals("C")) {
                    Sala1[i] = new Nodo(Sala1[i].A, Sala1[i].B, new Puesto(nombre, convSala1(asiento), true, calcuprecio1(convSala1(asiento))));
                } else {
                    System.out.println("Opcion no valida");
                }
            }
        } else if (peli == 2) {
            for (int i = 0; i < Integer.parseInt(asiento.substring(1)); i++) {
                if (asiento.substring(0).equals("A")){
                    Sala1[i] = new Nodo(new Puesto(nombre, convSala2(asiento), true, calcuprecio2(convSala2(asiento))),Sala1[i].B,Sala1[i].C);
                } else if (asiento.substring(0).equals("B")) {
                    Sala1[i] = new Nodo(Sala1[i].A, new Puesto(nombre, convSala2(asiento), true, calcuprecio2(convSala2(asiento))), Sala1[i].C);
                } else if (asiento.substring(0).equals("C")) {
                    Sala1[i] = new Nodo(Sala1[i].A, Sala1[i].B, new Puesto(nombre, convSala2(asiento), true, calcuprecio2(convSala2(asiento))));
                } else {
                    System.out.println("Opcion no valida");
                }
            }
        } else {
            System.out.println("Error de seleccion.");
        }
    }
}
