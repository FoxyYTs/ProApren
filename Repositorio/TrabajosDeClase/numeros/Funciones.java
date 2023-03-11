package Repositorio.TrabajosDeClase.numeros;

public class Funciones {
    
    /**
     * 
     * @param valor
     * @return octal
     */
    public String DaO(int valor){
        String octal = "";
        int residuo = 0;
    
        while(valor > 0) {
            residuo = valor % 8;
            octal = residuo + octal;
            valor = valor / 8;
        }
    
        return octal;
    }
    /**Decimal a Hexadecimal*/
    public void DaH(int valor){

    }

    public void DaB(int valor){//Decimal a Binario

    }

    public void OaD(int valor){//Octal a Decimal

    }

    public void OaH(int valor){//Octal a Hexadecimal

    }
    
    public void OaB(int valor){//Octal a Binario

    }

    public void HaO(int valor){//Hexadecimal a Octogonal

    }

    public void HaB(int valor){//Hexadecimal a Binario

    }

    public void HaD(int valor){//Hexadecimal a Decimal

    }

    public void BaO(int valor){//Binario a Octogonal

    }

    public void BaH(int valor){//Binario a Hexadecimal

    }

    public void BaD(int valor){//Binario a Decimal

    }

}
