package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio3;

public class Cola {
    static Nodo cabeza, cola;

    public static void push(boolean embarazo, int edad){
        if (embarazo) {
            System.out.println("Acaba de ingresar una embarazada");
        }
        System.out.println("Ingreso alguien con: " + edad + " Años");
        
        Nodo nuevo = new Nodo(embarazo, edad);
        if (cabeza == null && cola == null){
            cola = cabeza = nuevo;
        } else {
            cola.back = nuevo;
            nuevo.next = cola;
            cola = nuevo;
        }
        prioridad();
    }

    public void ingreso(){
        boolean embarazo = false;
        int edad = (int) (Math.floor(Math.random()*(100-18+1)+18)) ;

        if((int)(Math.random()*2) == 1){
            embarazo = true;
        }

        push(embarazo, edad);
    }

    public  void atender(){
        if (cabeza != null){
            cabeza.back = cabeza;
            System.out.println("Cliente atendido");
        }
    }

    public static void prioridad(){
        System.out.println("Se acaba de dar prioridad a alguien");
        if (cola.embarazo == true || cola.edad > 50){
            cola = cabeza.next;
            cabeza = cabeza.next;
            cola.back = null;
        }
    }

    public void eliminar(){
        if (cabeza != null && cola != null){
            cabeza = null;
            cola = null;
        }
    }
}
