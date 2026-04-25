// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-KOTLIN-001: ECB cipher mode in Kotlin

import javax.crypto.Cipher
import javax.crypto.SecretKey

class EcbCipher {

    fun encryptWithEcb(data: ByteArray, key: SecretKey): ByteArray {
        // TRIGGERS: Cipher.getInstance with ECB mode — leaks plaintext patterns
        val cipher = Cipher.getInstance("AES/ECB/PKCS5Padding")
        cipher.init(Cipher.ENCRYPT_MODE, key)
        return cipher.doFinal(data)
    }

    fun encryptDefault(data: ByteArray, key: SecretKey): ByteArray {
        // TRIGGERS: AES without mode defaults to ECB on most JVMs
        val cipher = Cipher.getInstance("AES/ECB/NoPadding")
        cipher.init(Cipher.ENCRYPT_MODE, key)
        return cipher.doFinal(data)
    }
}
