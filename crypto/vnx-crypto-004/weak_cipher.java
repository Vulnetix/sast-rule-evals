import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;

// VNX-CRYPTO-004: Broken cipher - DES
public class WeakCipher {
    public static byte[] encrypt(byte[] data) throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("DES");
        Cipher cipher = Cipher.getInstance("DES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, kg.generateKey());
        return cipher.doFinal(data);
    }
}
