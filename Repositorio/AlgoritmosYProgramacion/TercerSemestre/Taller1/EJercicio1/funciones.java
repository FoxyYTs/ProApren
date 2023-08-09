package AlgoritmosYProgramacion.TercerSemestre.Taller1.EJercicio1;

public class funciones {
    Nodo top;

    public funciones(){}

    public void insertar
    (String dato) {
        Nodo nuevo = new Nodo(dato);
        if (top == null) {
            top = nuevo;
        } else {
            top.back = nuevo;
            nuevo.next = top;
            top = top.back;
        }
    }

    public void mostrar() {
        Nodo pointer = top;
        while (pointer != null) {
            System.out.print(pointer.elemento + " ");
            pointer = pointer.next;
        }
    }

    public String igualador(){
        int pareopen = 0,coropen = 0,llavopen = 0;
        int pareclos = 0,corclos = 0,llavclos = 0;
        Nodo pointer = top;
        while (pointer != null) {
            System.out.print(pointer.elemento + " ");
            switch (pointer.elemento) {
                case "(":
                    pareopen++;
                    break;
                case "[":
                    coropen++;
                    break;
                case "{":
                    llavopen++;
                    break;
                case ")":
                    pareclos++;
                    break;
                case "]":
                    corclos++;
                    break;
                case "}":
                    llavclos++;
                    break;
                default:
                    break;
            }
            pointer = pointer.next;
        }
        if(pareopen == pareclos && coropen == corclos && llavopen == llavclos){
            return "Igualado";
        }else{
            return "Desigualado";
        }
    }
}
