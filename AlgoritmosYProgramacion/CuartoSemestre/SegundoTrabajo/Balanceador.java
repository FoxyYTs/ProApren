package AlgoritmosYProgramacion.CuartoSemestre.SegundoTrabajo;

public class Balanceador {
    public String balanceador(String cadena) {
        Pila list = new Pila();
        for (int i = 0; i < cadena.length(); i++) {
            if (cadena.charAt(i) == '(') {
                list.push(1);
            } else if (cadena.charAt(i) == ')'){
                list.pop();
            }
        }
        if (list.fill() != 0) {
            return "NO";
        } else {
            return "SI";
            
        }
    }
}
