import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Buffer {
    public static void main(String[] args) {
        String rutaEntrada = "/home/foxyyts/Proyectos/inventario.csv";
        String rutaSalida = "/home/foxyyts/Proyectos/invProcesado.csv";

        try (BufferedReader br = new BufferedReader(new FileReader(rutaEntrada));
             BufferedWriter bw = new BufferedWriter(new FileWriter(rutaSalida))) {

            String linea;
            boolean esCabecera = true;

            System.out.println("Procesando archivo y asignando clasificaciones...");
            
            int[] totales = null;
            int[] total = {0,0,0,0};

            while ((linea = br.readLine()) != null) {
                // Dividimos la línea por comas
                String[] columnas = linea.split(",");

                if (esCabecera) {
                    // Creamos la nueva cabecera: Referencia, Codigo, Clasificacion, Inventario
                    bw.write(columnas[0] + "," + columnas[1] + ",Clasificacion," + columnas[2]);
                    esCabecera = false;
                } else {
                    String referencia = columnas[0].replace(" ", "");
                    String codigo = columnas[1].replace(" ", "");
                    String inventario = columnas[2].replace(" ", "");
                    
                    // Obtenemos la clasificación basada en el primer caracter de la referencia
                    String clasificacion = obtenerClasificacion(referencia);
                    String codigoOptimo = recorte(codigo);
                    totales = acumulador(total, clasificacion, inventario);

                    // Escribimos la nueva línea con la columna insertada
                    bw.write(referencia + "," + codigoOptimo + "," + clasificacion + "," + inventario);
                }
                bw.newLine();
            }
            bw.write("Total Materna,Total Hombre,Total Dama,Total Infantil");
            bw.newLine();
            bw.write(totales[0] + "," + totales[1] + "," + totales[2] + "," + totales[3]);
            bw.newLine();

            System.out.println("Archivo procesado con éxito en: " + rutaSalida);

        } catch (IOException e) {
            System.out.println("Ocurrió un error: " + e.getMessage());
        }
    }

    private static int[] acumulador(int[] total, String clasificacion, String inventario){
        switch (clasificacion) {
            case "Linea Materna":
                total[0] += Integer.parseInt(inventario);
                break;
            case "Linea Hombre":
                total[1] += Integer.parseInt(inventario);
                break;
            case "Linea Dama":
                total[2] += Integer.parseInt(inventario);
                break;
            case "Linea Infantil":
                total[3] += Integer.parseInt(inventario);
                break;
        }

        return total;
    }

    private static String recorte(String codigo){
        String codigoF = "";
        if (codigo.charAt(0) == 'E'){
            for (int i = 0; i < 5; i++) {
                codigoF = codigoF + codigo.charAt(i);
            }
        }else{
            codigoF = codigo;
        }
        return codigoF;
    }

    private static String obtenerClasificacion(String referencia) {
        if (referencia == null || referencia.isEmpty()) return "Desconocido";
        
        char primerCaracter = referencia.charAt(0);

        switch (primerCaracter) {
            case '1': return "Linea Materna";
            case '2': return "Linea Hombre";
            case '3': return "Linea Dama";
            case '9': return "Linea Infantil";
            default: return "Otras Lineas";
        }
    }
}