package AlgoritmosYProgramacion.CuartoSemestre.Hashing;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Radix {

  public static String getSHA(String data) throws NoSuchAlgorithmException {
    MessageDigest digest = MessageDigest.getInstance("SHA-256");
    byte[] hash = digest.digest(data.getBytes());
    StringBuffer hexString = new StringBuffer();
    for (int i = 0; i < hash.length; i++) {
      String hex = Integer.toHexString(0xff & hash[i]);
      if(hex.length() == 1) hexString.append('0');
      hexString.append(hex);
    }
    return hexString.toString();
  }

  public static void main(String[] args) throws NoSuchAlgorithmException {
    String data = "hola";
    String sha256 = getSHA(data);
    System.out.println("SHA-256 hash of \"" + data + "\": " + sha256);
  }
}
