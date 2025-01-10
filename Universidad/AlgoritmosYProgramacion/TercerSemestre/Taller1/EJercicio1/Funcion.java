package AlgoritmosYProgramacion.TercerSemestre.Taller1.Ejercicio1;

public class Funcion {
    static Pila pila = new Pila();
    public boolean estaBalanceado(String entrada) {        
        char[] caracteres = entrada.toCharArray();
        for (int i = 0; i < caracteres.length; i++) {
            char caracter = caracteres[i];
            if (esCaracterValido(caracter)) {
                if (esCaracterDeApertura(caracter)) {
                    pila.push(caracter);
                } else if (esCaracterDeCierre(caracter)) {
                    if (pila.isEmpty() || !esPar(pila.pop(), caracter)) {
                        return false;
                    }
                }
            }
        }
        return pila.isEmpty();
    }
    
    public static boolean esCaracterValido(char c) {
        return c == '(' || c == ')' || c == '{' || c == '}' || c == '[' || c == ']';
    }
    
    public static boolean esCaracterDeApertura(char c) {
        return c == '(' || c == '{' || c == '[';
    }
    
    public static boolean esCaracterDeCierre(char c) {
        return c == ')' || c == '}' || c == ']';
    }
    
    public static boolean esPar(char abrir, char cerrar) {
        return (abrir == '(' && cerrar == ')') ||
               (abrir == '{' && cerrar == '}') ||
               (abrir == '[' && cerrar == ']');
    }
}
