package Repositorio.TrabajosDeClase.PromedioTemp;

public class PromTemp {
    public static void main(String[] args) {
        double tempDiaria[][] = new double[12][31];
        int diasMes[] = {31,30,31,30,31,30,31,31,30,31,30,31};
        String mes[] = {"Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"};
        double promedio[] = new double [12];
        double acum = 0;

        for (int i = 0; i < 12; i++) {
            acum = 0;
            for (int j = 0; j < diasMes[i]; j++) {
                System.out.print((j+1) + "|");
                acum += j+1;
            }
            if (diasMes[i] < 30) {
                System.out.println("" + 0);
            } else {
                System.out.println("" + (acum/diasMes[i]));
            }
        }
    }
}
