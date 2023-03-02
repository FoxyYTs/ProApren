package Repositorio.TrabajosDeClase.PromedioTemp;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        double temperaturas[][] = new double[12][31];

        int diasMes[] = {31,28,31,30,31,30,31,31,30,31,30,31};
        String mes[] = {"Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"};
        double promedio[] = new double[12];
        double g = 0;
        for (int i = 0; i < 12; i++) {
            g = 0;
            for (int j = 0; j < diasMes[i]; j++) {
                

                System.out.println("Ingresa la temperatura del dia " + (j+1) + " del mes " + (i+1));
                temperaturas[i][j] = j+1;//Integer.parseInt(leer.nextLine())

                if(diasMes[i] == 28){
                    g = 0;
                }else {
                    g += temperaturas[i][j];
                }
                System.out.println(g);
            }
        }
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < diasMes[i]; j++) {
                System.out.print(temperaturas[i][j] + "|");

            }
            promedio[i] = g/diasMes[i];
            
            System.out.println("Promedio: " + promedio[i]);
        }

    }
}

