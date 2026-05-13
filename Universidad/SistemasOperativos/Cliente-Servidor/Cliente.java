import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Cliente {
    public static void main(String[] args) {
        String host = "localhost";
        int puerto = 5000;

        Thread cliente1Thread = new Thread(() -> Clientes(host, puerto, "Mensaje del cliente 1"));
        Thread cliente2Thread = new Thread(() -> Clientes(host, puerto, "Mensaje del cliente 2"));
        Thread cliente3Thread = new Thread(() -> Clientes(host, puerto, "Mensaje del cliente 3"));

        cliente1Thread.start();
        cliente2Thread.start();
        cliente3Thread.start();
        
    }

    private static void Clientes(String host, int puerto, String mensaje) {
        try (Socket socket = new Socket(host, puerto)) {
            System.out.println("Conectado al servidor en el puerto " + puerto);

            PrintWriter salida = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            salida.println(mensaje);

            String respuesta = entrada.readLine();
            System.out.println("Respuesta del servidor: " + respuesta);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
