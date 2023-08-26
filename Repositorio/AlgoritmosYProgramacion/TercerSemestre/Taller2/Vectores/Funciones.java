package AlgoritmosYProgramacion.TercerSemestre.Taller2.Vectores;

import java.util.Vector;

public class Funciones {
    double pBase = 85000,fuel = pBase*0.15, admin = pBase*0.07, seguro = pBase*0.10, total = pBase + fuel + admin + seguro, vipP = (total*0.65) + total;

    int sillaVip = 5, silla = 8, cantSilla = sillaVip + silla;

    int contadorVip = 0, contadorOcupado = 0;

    Vector<Nodo> victor = new Vector<>();

    public String valor(){
        return "El Valor Base del tiquete es \nBASE: " + (int) pBase + "\nCOMBUSTIBLE 15%: " + (int) fuel + "\nTASA ADMINISTRACION 7%: " + (int) admin + "\nSEGURO 10%: " + (int) seguro + "\nTOTAL: " + (int) total + "\nVIP 65% + TOTAL: " + (int) vipP ;
    }

    public void disponibilidad(){
        if (contadorOcupado <= 0) {
            System.out.println("El Avion esta Vacio");
            return;
        }
        for (int i = 0; i < contadorOcupado; i++) {
            System.out.println("Puesto #" + i+1 + " Nombre Pasajero: " + victor.get(i).dueño + " VIP: " + victor.get(i).vip);
        }
    }

    public void compra(String nombre, Boolean vip){
        if (vip) {
            System.out.println("Se a Comprado un Tiqued a nombre: " + nombre + "\nVIP: " + vip + "\nTOTAL: " + vipP);
            contadorVip++;
            victor.add(new Nodo(nombre, vip, vipP));
            contadorOcupado++;
        } else {
            System.out.println("Se a Comprado un Tiqued a nombre: " + nombre + "\nVIP: " + vip + "\nTOTAL: " + total);
            victor.add(new Nodo(nombre, vip, total));
            contadorOcupado++;
        }
    }
}
