import java.io.*;
import java.net.*;

public class Servidor {
    public static void main(String[] args) {
        int puerto = 5000;
        
        try (ServerSocket serverSocket = new ServerSocket(puerto)) {
            System.out.println("Servidor multihilo escuchando en el puerto " + puerto);

            while (true) {
                // El servidor se bloquea aquí hasta que llega una nueva conexión
                Socket clientSocket = serverSocket.accept();
                System.out.println("Nuevo cliente conectado: " + clientSocket.getInetAddress());

                // Creamos un hilo nuevo para manejar la comunicación con este cliente
                Thread hiloCliente = new Thread(new ManejadorCliente(clientSocket));
                hiloCliente.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

/**
 * Clase encargada de la lógica de comunicación con un cliente específico
 */
class ManejadorCliente implements Runnable {
    private Socket socket;

    public ManejadorCliente(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        try (
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter salida = new PrintWriter(socket.getOutputStream(), true)
        ) {
            String mensajeCliente = in.readLine();
            System.out.println("Hilo [" + Thread.currentThread().getId() + "] recibió: " + mensajeCliente);
            
            // Simulamos un pequeño retraso para notar la concurrencia
            Thread.sleep(1000); 
            
            salida.println("Servidor procesó: " + mensajeCliente);

        } catch (IOException | InterruptedException e) {
            System.err.println("Error en la comunicación con el cliente: " + e.getMessage());
        } finally {
            try {
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}