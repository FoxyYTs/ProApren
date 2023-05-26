package TrabajosDeClase.numeros;

public class Funciones {
    
    public String DaO(String valors){
        int decimal = Integer.parseInt(valors);

        String octal = Integer.toOctalString(decimal);

        return octal;
    }

    public String DaH(String valors){
        int decimal = Integer.parseInt(valors);

        String hexadecimal = Integer.toHexString(decimal);

        return hexadecimal;

    }

    public String DaB(String valors){
        int decimal = Integer.parseInt(valors);

        String binario = Integer.toBinaryString(decimal);
        
        return binario;
    }

    public String OaD(String valors){//Octal a Decimal
        String decimal = "" + Integer.parseInt(valors, 8);
        
        return decimal;
    }

    public String OaH(String valors){//Octal a Hexadecimal
        int decimal = Integer.parseInt(OaD(valors));
        
        String hexadecimal = Integer.toHexString(decimal);
        
        return hexadecimal;
    }

    public String OaB(String valors){//Octal a Binario
        int decimal = Integer.parseInt(OaD(valors));

        String octal = Integer.toBinaryString(decimal);

        return octal;
    }

    public String HaO(String valors){//Hexadecimal a Octogonal
        String decimal = "" + Integer.parseInt(valors, 8);

        String octal = DaO(decimal);

        return octal;
    }

    public String HaB(String valors){//Hexadecimal a Binario
        String decimal = "" + Integer.parseInt(valors, 16);

        String binario = DaB(decimal);

        return binario;
    }

    public String HaD(String valors){//Hexadecimal a Decimal
        String decimal = "" + Integer.parseInt(valors, 16);

        return decimal;
    }

    public String BaO(String valors){//Binario a Octogonal
        String decimal = "" + Integer.parseInt(valors, 2);

        String octal = DaO(decimal);

        return octal;
    }

    public String BaH(String valors){//Binario a Hexadecimal
        String decimal = "" + Integer.parseInt(valors, 2);

        String hexadecimal = DaH(decimal);

        return hexadecimal;
    }

    public String BaD(String valors){//Binario a Decimal
        String decimal = "" + Integer.parseInt(valors, 2);

        return decimal;
    }

}
