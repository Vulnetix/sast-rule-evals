// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-019: Hardcoded cryptographic key literal

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

public class HardcodedCryptoKey {

    // TRIGGERS: hardcoded AES key literal
    private static final String SECRET_KEY = "MySuperSecretKey";

    // TRIGGERS: hardcoded key passed to SecretKeySpec
    public SecretKey getKey() {
        return new SecretKeySpec("AES_KEY_1234567".getBytes(), "AES");
    }

    public byte[] encrypt(byte[] data) throws Exception {
        SecretKey key = new SecretKeySpec(SECRET_KEY.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        return cipher.doFinal(data);
    }
}
