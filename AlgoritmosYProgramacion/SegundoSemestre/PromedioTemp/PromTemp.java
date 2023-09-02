package AlgoritmosYProgramacion.SegundoSemestre.PromedioTemp;

import java.util.Scanner;

public class PromTemp {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double tempDiaria[][] = new double[12][31];
        int diasMes[] = {31,28,31,30,31,30,31,31,30,31,30,31}, minM = 0, maxM = 0;
        String mes[] = {"Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"};
        double promedio[] = new double [12];
        double acum = 0,max = -1 ,min = 100000000, h=0;

        for (int i = 0; i < 12; i++) {
            acum = 0;
            for (int j = 0; j < diasMes[i]; j++) {

                h++;
                System.out.println("Que temperatura hizo el dia " + (j+1) + " de " + mes[i] + ": " + (j+1));
                tempDiaria[i][j] = j+1;
                
                acum += tempDiaria[i][j];
                promedio[i] = acum/diasMes[i];
            }
            System.out.println("Promedio: " + promedio[i]);
        }
        for (int i = 0; i < 12; i++) {
            if (max < promedio[i]){
                max = promedio[i];
                maxM = i;
            }
            if (min > promedio[i] && promedio[i] != 0){
                min = promedio[i];
                minM = i;
            }
        }
        System.out.println("El mes con mas calor es: " + mes[maxM] + " con una temperatura de: " + max + "\ny el mas frio es: " + mes[minM] + " con una temperatura de: " + min);
        
        for (int i = 0; i < 12; i++) {
            int dias = 0;
            int diasReales = tempDiaria[i].length;
            for (int j = 0; j < diasReales; j++) {
                if(tempDiaria[i][j] > promedio[i]){
                    dias++;
                    System.out.println("El día " + (j + 1) + " de " + mes[i] + " estuvo por encima del promedio");
                }
            }
            if(dias == 0){
                System.out.println("No hubo días por encima del promedio en " + mes[i]);
            }
        }

    }
}
