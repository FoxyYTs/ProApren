import java.time.LocalDateTime;

public class Eventos {
    private String titulo;
    private LocalDateTime fechaHoraInicio;
    private LocalDateTime fechaHoraFin;
    public Eventos next;

    public Eventos(String titulo, LocalDateTime fechaHoraInicio, LocalDateTime fechaHoraFin) {
        this.titulo = titulo;
        this.fechaHoraInicio = fechaHoraInicio;
        this.fechaHoraFin = fechaHoraFin;
        this.next = null;
    }

    public String getTitulo() {
        return titulo;
    }

    public LocalDateTime getFechaHoraInicio() {
        return fechaHoraInicio;
    }

    public LocalDateTime getFechaHoraFin() {
        return fechaHoraFin;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setFechaHoraInicio() {
        this.fechaHoraInicio = fechaHoraInicio;
    }

    public void setFechaHoraFin() {
        this.fechaHoraFin = fechaHoraFin;
    }
}