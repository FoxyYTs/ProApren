import java.time.LocalDateTime;

public class Calendario{

    public Eventos headEvento;
    public Eventos pointerEvento;
    public Recordatorios headRecordatorio;
    public Recordatorios pointerRecordatorio;

    public void insertarEventos(String titulo, LocalDateTime fechaHoraInicio, LocalDateTime fechaHoraFin) {
        Eventos nuevo = new Eventos(titulo, fechaHoraInicio, fechaHoraFin);
        if (headEvento == null) {
            headEvento = nuevo;
        } else {
            Eventos pointerEventos = headEvento;
            while (pointerEventos.next != null) {
                pointerEventos = pointerEventos.next;
            }
            pointerEventos.next = nuevo;
        }
    }

    public void eliminarEvento(String titulo) {
        if (headEvento == null) {
            return;
        }
        if (headEvento.getTitulo() == titulo) {
            headEvento = headEvento.next;
            return;
        }
        Eventos pointerEvento = headEvento;
        while (pointerEvento.next.getTitulo() != titulo && pointerEvento.next != null) {
            pointerEvento = pointerEvento.next;
        }
        if (pointerEvento.next != null) {
            pointerEvento.next = pointerEvento.next.next;
        }
    }

    public void mostrarEventos() {
        Eventos pointerEventos = headEvento;
        while (pointerEventos != null) {
            //configuracion.calendarioMostrarEvento(pointerEventos.getTitulo(), pointerEventos.getFechaHoraInicio(),pointerEventos.getFechaHoraFin());
            pointerEventos = pointerEventos.next;
        }
        System.out.println();
    }

    public void insertarRecordatorios(String mensaje, LocalDateTime fechaHora) {
        Recordatorios nuevo = new Recordatorios(mensaje, fechaHora);
        if (headRecordatorio == null) {
            headRecordatorio = nuevo;
        } else {
            Recordatorios pointerRecordatorio = headRecordatorio;
            while (pointerRecordatorio.next != null) {
                pointerRecordatorio = pointerRecordatorio.next;
            }
            pointerRecordatorio.next = nuevo;
        }
    }
    
    public void eliminarRecordatorios(String mensaje) {
        if (headRecordatorio == null) {
            return;
        }
        if (headRecordatorio.getMensaje() == mensaje) {
            headRecordatorio = headRecordatorio.next;
            return;
        }
        Recordatorios pointerRecordatorio = headRecordatorio;
        while (pointerRecordatorio.next.getMensaje() != mensaje && pointerRecordatorio.next != null) {
            pointerRecordatorio = pointerRecordatorio.next;
        }
        if (pointerRecordatorio.next != null) {
            pointerRecordatorio.next = pointerRecordatorio.next.next;
        }
    }
    
    public void mostrarRecordatorios() {
        Recordatorios pointerRecordatorio = headRecordatorio;
        while (pointerRecordatorio != null) {
            //configuracion.calendarioMostrarRecordatorios(pointerRecordatorio.getMensaje(),pointerRecordatorio.getFechaHora());
            pointerRecordatorio = pointerRecordatorio.next;
        }
        System.out.println();
    }

}
