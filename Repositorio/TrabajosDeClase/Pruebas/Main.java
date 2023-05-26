package TrabajosDeClase.Pruebas;

public class Main {
    public static void main(String[] args) {
        double[] promTemperaturaMes = new double[12];

        double[][] temperaturas = matriz();
        promedioDeTemperaturaMes(temperaturas, promTemperaturaMes);
        for (int i = 0; i < 12; i++) {
            System.out.println("Promedio " + traducirMes(i+1) + ": " + promTemperaturaMes[i]);
        }
        double promedioTempMasBaja = promTemperaturaMes[0];
        double promedioTempMasAlta = promTemperaturaMes[0];
        for (int i = 1; i < 12; i++) {
            if(promedioTempMasBaja > promTemperaturaMes[i]){
                promedioTempMasBaja = promTemperaturaMes[i];
            }
            if(promedioTempMasAlta < promTemperaturaMes[i]){
                promedioTempMasAlta = promTemperaturaMes[i];
            }

        }

        System.out.println("La Temperatura Mas Baja es " + promedioTempMasBaja);
        System.out.println("La Temperatura Mas Alta es " + promedioTempMasAlta);

        int fila = 12, columna = 30;
        for (int i = 0; i < fila; i++) {
            for (int j = 0; j < columna; j++) {
                if (temperaturas[i][j] > promTemperaturaMes[i]){
                    System.out.println("La Temperatura Para El Dia " + j + " En El Mes  " + traducirMes(i+1) + " Fue Mas Alta Que El Promedio " + promTemperaturaMes[i] );
                }
            }
        }
    }

    public static double[][] matriz() {

        int fila = 12, columna = 30;
        double[][] temperaturas = new double[fila][columna];

        for (int i = 0; i < fila; i++) {
            for (int j = 0; j < columna; j++) {
                temperaturas[i][j] = (Math.random() * 30) - 4;
            }
        }
        return temperaturas;

    }

    public static double[] promedioDeTemperaturaMes(double[][] temperaturas, double[] promTemperaturaMes){
        int fila = 12, columna = 30;
        int contadorFila = 0, contadorColumna = 0;
        while(contadorFila < fila){
            while(contadorColumna < columna){
                promTemperaturaMes[contadorFila] += temperaturas[contadorFila][contadorColumna];
                contadorColumna++;
            }
            promTemperaturaMes[contadorFila] = promTemperaturaMes[contadorFila] / 30;
            contadorFila++;
            contadorColumna = 0;
        }

        return promTemperaturaMes;
    }

    public static String traducirMes(int numeroMes){
        String mesTraducido;
        switch (numeroMes){
            case 1:
                mesTraducido = "Enero";
                break;
            case 2:
                mesTraducido = "Febrero";
                break;
            case 3:
                mesTraducido = "Marzo";
                break;
            case 4:
                mesTraducido = "Abril";
                break;
            case 5:
                mesTraducido = "Mayo";
                break;
            case 6:
                mesTraducido = "Junio";
                break;
            case 7:
                mesTraducido = "Julio";
                break;
            case 8:
                mesTraducido = "Agosto";
                break;
            case 9:
                mesTraducido = "Septiembre";
                break;
            case 10:
                mesTraducido = "Octubre";
                break;
            case 11:
                mesTraducido = "noviembre";
                break;
            case 12:
                mesTraducido = "diciembre";
                break;
            default:
                mesTraducido = "";
                break;
        }
        return mesTraducido;
    }

}
