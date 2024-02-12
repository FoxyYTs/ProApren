package AlgoritmosYProgramacion.CuartoSemestre.PrimerTrabajo;

import java.io.*;

public class Main {

    public static void main(String[] args) {
        System.err.println(readTB());
    }
    private static int readTB() {
        try {
            BufferedReader input = new BufferedReader(new FileReader("./AlgoritmosYProgramacion/CuartoSemestre/PrimerTrabajo/Tetris.txt"));
            String tbMaxScore = input.readLine();
            input.close();
            return Integer.parseInt(tbMaxScore);
        } catch (IOException e) {
            return -1;
        } catch (NumberFormatException e) {
            return -1;
        }
    }

    private static void writeTB(int tbScore) {
        try {
            File UIFile = new File("./AlgoritmosYProgramacion/CuartoSemestre/PrimerTrabajo/Tetris.txt   ");
            if (!UIFile.exists()) {
                UIFile.createNewFile();
            }
            FileWriter filewriter = new FileWriter(UIFile.getAbsoluteFile());
            BufferedWriter outputStream = new BufferedWriter(filewriter);
            outputStream.write(String.valueOf(tbScore));
            outputStream.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
