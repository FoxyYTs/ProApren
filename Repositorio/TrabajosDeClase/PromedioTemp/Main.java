package Repositorio.TrabajosDeClase.PromedioTemp;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);

        double temperaturas[][] = new double[12][31];

        int diasMes[] = {31,28,31,30,31,30,31,31,30,31,30,31};
        double promedio[] = new double[12];
        int x = 1;
        for (int i = 0; i < 1; i++) {
            for (int j = 0; j < diasMes[i]; j++) {

                System.out.println("Ingresa la temperatura del dia " + (j+1) + " del mes " + (i+1));
                temperaturas[i][j] = j+1;//Integer.parseInt(leer.nextLine())

                if(diasMes[i] <= 29)
                promedio[i] += temperaturas[i][j]; 
            }
        }
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < diasMes[i]; j++) {
                System.out.print(temperaturas[i][j] + "|");
            }
            System.out.println("Promedio: " + promedio[i]);
        }

    }
}

