// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-020: Static IV reuse in block cipher

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;

public class StaticIV {

    // TRIGGERS: static final IV byte array
    private static final byte[] IV = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};

    public byte[] encrypt(byte[] plaintext, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        // VULNERABLE: static IV reused for every encryption operation
        cipher.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(IV));
        return cipher.doFinal(plaintext);
    }

    public byte[] encryptWithLiteralIv(byte[] plaintext, SecretKey key) throws Exception {
        // TRIGGERS: IvParameterSpec constructed from a string literal
        IvParameterSpec ivSpec = new IvParameterSpec("1234567890123456".getBytes());
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
        return cipher.doFinal(plaintext);
    }
}
