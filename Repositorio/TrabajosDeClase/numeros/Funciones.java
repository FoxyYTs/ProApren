package Repositorio.TrabajosDeClase.numeros;

public class Funciones {
    
    /**
     * Decimal a Octal
     * 
     * @param valor
     * 
     * @return String
     */
    public String DaO(String valors){
        String octal = "";
        int valor = Integer.parseInt(valors);
        int residuo = 0;
    
        while(valor > 0) {
            residuo = valor % 8;
            octal = residuo + octal;
            valor = valor / 8;
        }
    
        return octal;
    }
    /**
     * Decimal a Hexadecimal
     * 
     * @param valor
     * 
     * @return String
     */
    public String DaH(String valors){
        String hexadecimal = "";
        int decimal = Integer.parseInt(valors);
        int residuo = 0;
        
        while(decimal > 0) {
            residuo = decimal % 16;
            if(residuo < 10) {
                hexadecimal = residuo + hexadecimal;
            } else {
                char letraHexadecimal = (char) ('A' + (residuo - 10));
                hexadecimal = letraHexadecimal + hexadecimal;
            }
            decimal = decimal / 16;
        }
    
    return hexadecimal;

    }
    /**
     * Decimal a Binario
     * 
     * @param valor
     * 
     * @return String
     */
    public String DaB(String valors){//Decimal a Binario
        String binario = "";
        return binario;
    }
    /**
     * Octal a Decimal
     * 
     * @param valor
     * 
     * @return String
     */
    public String OaD(String valors){//Octal a Decimal
        String decimal = "";
        return decimal;
    }
    /**
     * Octal a Hexadecimal
     * 
     * @param valor
     * 
     * @return String
     */
    public String OaH(String valors){//Octal a Hexadecimal
        String hexadecimal = "";
        return hexadecimal;
    }
    /**
     * Octal a Binario
     * 
     * @param valor
     * 
     * @return String
     */
    public String OaB(String valors){//Octal a Binario
        String binario = "";
        return binario;
    }
    /**
     * Hexadecimal a Octal
     * 
     * @param valor
     * 
     * @return String
     */
    public String HaO(String valors){//Hexadecimal a Octogonal
        String octal = "";
        return octal;
    }
    /**
     * Hexadecimal a Binario
     * 
     * @param valor
     * 
     * @return String
     */
    public String HaB(String valors){//Hexadecimal a Binario
        String binario = "";
        return binario;
    }
    /**
     * Hexadecimal a Decimal
     * 
     * @param valor
     * 
     * @return String
     */
    public String HaD(String valors){//Hexadecimal a Decimal
        String decimal = "";
        return decimal;
    }
    /**
     * Binario a Octal
     * 
     * @param valor
     * 
     * @return String
     */
    public String BaO(String valors){//Binario a Octogonal
        String octal = "";
        return octal;
    }
    /**
     * Binario a Hexadecimal
     * 
     * @param valor
     * 
     * @return String
     */
    public String BaH(String valors){//Binario a Hexadecimal
        String hexadecimal = "";
        return hexadecimal;
    }
    /**
     * Binario a Decimal
     * 
     * @param valor
     * 
     * @return String
     */
    public String BaD(String valors){//Binario a Decimal
        String decimal = "";
        return decimal;
    }

}
