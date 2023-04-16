import java.time.LocalDateTime;

public class Recordatorios {
    private String mensaje;
    private LocalDateTime fechaHora;
    public Recordatorios next;

    public Recordatorios(String mensaje, LocalDateTime fechaHora){
        this.mensaje = mensaje;
        this.fechaHora = fechaHora;
        this.next = null;
    }

    public String getMensaje(){
        return mensaje;
    }

    public LocalDateTime getFechaHora(){
        return fechaHora;
    }

    public void setMensaje(String mensaje){
        this.mensaje = mensaje;
    }

    public void setFechaHora(LocalDateTime fechaHora){
        this.fechaHora = fechaHora;
    }
}
