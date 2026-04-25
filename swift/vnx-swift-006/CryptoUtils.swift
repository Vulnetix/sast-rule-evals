// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-SWIFT-006: Insecure random functions in security context

import Foundation

class CryptoUtils {
    // VULNERABLE: arc4random_uniform for token generation
    func generateOTPCode() -> String {
        var token = ""
        for _ in 0..<6 {
            token += String(arc4random_uniform(10))
        }
        return token
    }

    // VULNERABLE: arc4random_buf for nonce generation
    func generateNonce() -> Data {
        var nonce = Data(count: 16)
        nonce.withUnsafeMutableBytes { bytes in
            arc4random_buf(bytes.baseAddress!, 16)
        }
        return nonce
    }

    // VULNERABLE: rand() for password salt generation
    func generateSalt() -> Int32 {
        // This salt is predictable
        let salt = rand()
        return salt
    }
}
