package AlgoritmosYProgramacion.TercerSemestre.Quiz1;

public class Funciones {
    Nodo[] Sala1 = new Nodo[8];

    String[] pS1TOP = {"","\t 0","\t 1","\t 2","\t 3","\t 4","\t 5","\t 6"};
    String[] pS1A = {"A","\t|G|","\t|G|","\t|M|","\t|M|","\t|M|","\t|G|","\t|G|"};
    String[] pS1B = {"B","\t|D|","\t|G|","\t|G|","\t|G|","\t|G|","\t|G|","\t|D|"};
    String[] pS1C = {"C","\t|D|","\t|G|","\t|S|","\t|S|","\t|S|","\t|G|","\t|D|"};
    
    //A2-3-4 Movilidad reducida
    //B0-6 Descuento 10%
    //C0-6 Descuento 10% C2-3-4 Sonido y Vibrador 
    Nodo[] Sala2 = new Nodo[8];

    String[] pS2TOP = {"","\t 0","\t 1","\t 2","\t 3","\t 4","\t 5","\t 6"};
    String[] pS2A = {"A","\t|D|","\t|G|","\t|M|","\t|M|","\t|M|","\t|G|","\t|D|"};
    String[] pS2B = {"B","\t|G|","\t|G|","\t|S|","\t|S|","\t|S|","\t|G|","\t|G|"};
    String[] pS2C = {"C","\t|G|","\t|S|","\t|S|","\t|S|","\t|S|","\t|S|","\t|G|"};
    //A0-6 Descuento 10% A2-3-4 Movilidad reducida
    //B2-3-4 Sonido y Vibrador
    //C0-6 Descuento 10% C1-2-3-4-5 Sonido y Vibrador

    public void inicio(){
        if (Sala1[1] == null){
            for (int i = 0; i < 8; i++) {
            Sala1[i] = new Nodo(new Puesto("VACIO", conversor(pS1TOP[i]), pS1TOP[i], calcuprecio2(conversor(pS1TOP[i]))), new Puesto("VACIO", conversor(pS1A[i]), pS1A[i], calcuprecio2(conversor(pS1A[i]))), new Puesto("VACIO", conversor(pS1B[i]), pS1B[i], calcuprecio2(conversor(pS1B[i]))) ,new Puesto("VACIO", conversor(pS1C[i]), pS1C[i], calcuprecio2(conversor(pS1C[i]))));
            }
        }

        if (Sala2[1] == null){
            for (int i = 0; i < 8; i++) {
            Sala2[i] = new Nodo(new Puesto("VACIO", conversor(pS2TOP[i]), pS2TOP[i], calcuprecio2(conversor(pS2TOP[i]))), new Puesto("VACIO", conversor(pS2A[i]), pS2A[i], calcuprecio2(conversor(pS2A[i]))), new Puesto("VACIO", conversor(pS2B[i]), pS2B[i], calcuprecio2(conversor(pS2B[i]))) ,new Puesto("VACIO", conversor(pS2C[i]), pS2C[i], calcuprecio2(conversor(pS2C[i]))));
            }
        }
    }

    public void mapaSala1(){
        for (int i = 0; i < 8; i++) {
            System.out.print(Sala1[i].getTOP().getOcupado());
        }
        System.out.println("\n");
        for (int i = 0; i < 8; i++) {
            System.out.print(Sala1[i].getA().getOcupado());
        }
        System.out.println("\n");
        for (int i = 0; i < 8; i++) {
            System.out.print(Sala1[i].getB().getOcupado());
        }
        System.out.println("\n");
        for (int i = 0; i < 8; i++) {
            System.out.print(Sala1[i].getC().getOcupado());
        }
    }

    public void mapaSala2(){
        for (int i = 0; i < 8; i++) {
            System.out.print(Sala2[i].getTOP().getOcupado());
        }
        System.out.println("\n");
        for (int i = 0; i < 8; i++) {
            System.out.print(Sala2[i].getA().getOcupado());
        }
        System.out.println("\n");
        for (int i = 0; i < 8; i++) {
            System.out.print(Sala2[i].getB().getOcupado());
        }
        System.out.println("\n");
        for (int i = 0; i < 8; i++) {
            System.out.print(Sala2[i].getC().getOcupado());
        }
    }

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

    public String conversor(String asiento){
        if (asiento.equals("|M|")){
            return "Movilidad Reducida";
        } else if (asiento.equals("\t|D|")){
            return "Descuento 10%";
        } else if (asiento.equals("\t|S|")){
            return "Sonido y Vibracion";
        } else if (asiento.equals("\t|G|")){
            return "General";
        } else {
            return "ERROR";
        }
    }

    public void reseva(int peli, String fila, int columna, String nombre){
        if (peli == 1) {
            if (fila.toUpperCase().equals("A")){
                Sala1[columna+1].getA().setCliente(nombre);
                Sala1[columna+1].getA().setOcupado("\t|X|");
            } else if (fila.toUpperCase().equals("B")) {
                Sala1[columna+1].getB().setCliente(nombre);
                Sala1[columna+1].getB().setOcupado("\t|X|");
            } else if (fila.toUpperCase().equals("C")) {
                Sala1[columna+1].getC().setCliente(nombre);
                Sala1[columna+1].getC().setOcupado("\t|X|");
            } else {
                System.out.println("Opcion no valida");
            }
            
        } else if (peli == 2) {
            if (fila.toUpperCase().equals("A")){
                Sala2[columna+1].getA().setCliente(nombre);
                Sala2[columna+1].getA().setOcupado("\t|X|");
            } else if (fila.toUpperCase().equals("B")) {
                Sala2[columna+1].getB().setCliente(nombre);
                Sala2[columna+1].getB().setOcupado("\t|X|");
            } else if (fila.toUpperCase().equals("C")) {
                Sala2[columna+1].getC().setCliente(nombre);
                Sala2[columna+1].getC().setOcupado("\t|X|");
            } else {
                System.out.println("Opcion no valida");
            }
        } else {
            System.out.println("Error de seleccion.");
        }
        
    }
}
