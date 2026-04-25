// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-KOTLIN-002: RSA key smaller than 2048 bits

import java.security.KeyPairGenerator

class WeakRsaKey {

    fun generateLegacyKeyPair() {
        // TRIGGERS: RSA key initialized with only 1024 bits
        val keyGen = KeyPairGenerator.getInstance("RSA")
        keyGen.initialize(1024)
        val keyPair = keyGen.generateKeyPair()
    }

    fun generateTinyKeyPair() {
        // TRIGGERS: RSA key initialized with 512 bits
        val kpg = KeyPairGenerator.getInstance("RSA")
        kpg.initialize(512)
        val pair = kpg.generateKeyPair()
    }
}
