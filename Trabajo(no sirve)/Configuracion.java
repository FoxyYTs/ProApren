import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Configuracion {
    private String formatoFecha = "";
    private String idioma;

    public Configuracion(String formatoFecha, String idioma) {
        this.formatoFecha = formatoFecha;
        this.idioma = idioma;
    }

    public String getFormatoFecha() {
        return formatoFecha;
    }

    public String getIdioma() {
        return idioma;
    }

    public void setFormatoFecha(String formatoFecha) {
        this.formatoFecha = formatoFecha;
    }

    public void setIdioma(String idioma) {
        this.idioma = idioma;
    }

    public String fechaHora(LocalDateTime fechaHoraActual) {
        DateTimeFormatter formatoFechaHora = DateTimeFormatter.ofPattern(formatoFecha);
        String fechaHoraFormateada = fechaHoraActual.format(formatoFechaHora);
        return fechaHoraFormateada;
    }

    public void calendarioMostrarEvento(String titulo, LocalDateTime fechaHoraInicio, LocalDateTime fechaHoraFinal) {
        if (idioma == "en") {
            System.out.println("Event [title: " + titulo + ", Start date and time: " + fechaHoraInicio + ", End date and time: " + fechaHoraFinal + "]");
        } else {
            System.out.println("Evento [titulo: " + titulo + ", Fecha y Hora de inicio: " + fechaHoraInicio + ", Fecha y hora de Fin: " + fechaHoraFinal + "]");
        }
    }

    public void calendarioMostrarRecordatorios(String mensaje, LocalDateTime fechaHora) {
        if (idioma == "en") {
            System.out.println("Reminder [message: " + mensaje + ", Date and Time: " + fechaHora + "]");
        } else {
            System.out.println("Recordatorio [mensaje: " + mensaje + ", Fecha y Hora: " + fechaHora + "]");
        }
    }

    public void gruposMostrarContactos(String nombre, String apellido, String telefono, String correo) {
        if (idioma == "en") {
            System.out.println("Contact [name: " + nombre + ", last name: " + apellido + ", phone: " + telefono + ", email: " + correo + "]");
        } else {
            System.out.println("Contacto [nombre: " + nombre + ", apellido: " + apellido + ", telefono: " + telefono + ", correo: " + correo + "]");
        }
    }

    public void agendaMostrarContactos(String nombre, String apellido, String telefono, String correo) {
        if (idioma == "en") {
            System.out.println("Contact [name: " + nombre + ", last name: " + apellido + ", phone: " + telefono + ", email: " + correo + "]");
        } else {
            System.out.println("Contacto [nombre: " + nombre + ", apellido: " + apellido + ", telefono: " + telefono + ", correo: " + correo + "]");
        }
    }

    public void agendaMostrarGrupo(String nombre) {
        if (idioma == "en") {
            System.out.println("Contact [name: " + nombre + "]");
        } else {
            System.out.println("Contacto [nombre: " + nombre + "]");
        }
    }

}