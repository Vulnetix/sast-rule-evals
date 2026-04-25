// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-KOTLIN-005: MD5 or SHA-1 used as cryptographic hash in Kotlin

import java.security.MessageDigest
import org.apache.commons.codec.digest.DigestUtils

class WeakHash {

    fun hashPassword(password: String): String {
        // TRIGGERS: MD5 for password hashing — completely broken
        val md = MessageDigest.getInstance("MD5")
        return md.digest(password.toByteArray()).joinToString("") { "%02x".format(it) }
    }

    fun checksumFile(data: ByteArray): String {
        // TRIGGERS: SHA-1 for integrity check — collision resistant is broken
        val sha1 = MessageDigest.getInstance("SHA-1")
        return sha1.digest(data).joinToString("") { "%02x".format(it) }
    }

    fun legacyChecksum(content: String): String {
        // TRIGGERS: DigestUtils.md5Hex — Apache Commons MD5 helper
        return DigestUtils.md5Hex(content)
    }
}
