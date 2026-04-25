// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-018: RSA cipher without OAEP padding

import javax.crypto.Cipher;
import java.security.PublicKey;

public class InsecureRSA {

    public byte[] encryptWithPkcs1(byte[] plaintext, PublicKey publicKey) throws Exception {
        // VULNERABLE: PKCS#1 v1.5 padding is susceptible to padding oracle attacks
        Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        return cipher.doFinal(plaintext);
    }

    public byte[] encryptNoPadding(byte[] plaintext, PublicKey publicKey) throws Exception {
        // VULNERABLE: no padding at all — textbook RSA is completely insecure
        Cipher cipher = Cipher.getInstance("RSA/ECB/NoPadding");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        return cipher.doFinal(plaintext);
    }
}
