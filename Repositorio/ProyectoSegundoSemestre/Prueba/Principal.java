import java.util.Scanner;
import java.time.LocalDateTime;

public class Principal {
    FechaFormato fachero = new FechaFormato();
    Scanner leer = new Scanner(System.in);
    private String formato,idioma;

    public Principal(String formato, String idioma) {
        this.formato = formato;
        this.idioma = idioma;
    }
}
