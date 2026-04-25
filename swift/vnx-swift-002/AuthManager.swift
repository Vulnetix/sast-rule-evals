// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-SWIFT-002: NSLog with sensitive data

import Foundation

class AuthManager {
    func login(username: String, password: String) -> Bool {
        // VULNERABLE: Logging password to system console
        NSLog("Attempting login for user: %@ with password: %@", username, password)

        let result = authenticate(user: username, pass: password)

        // VULNERABLE: Logging auth token
        if let token = result {
            NSLog("Received auth token: %@", token)
        }
        return result != nil
    }

    func refreshToken(token: String) {
        // VULNERABLE: Logging secret token
        NSLog("Refreshing token: %@", token)
        // ... refresh logic ...
    }

    private func authenticate(user: String, pass: String) -> String? {
        return nil // placeholder
    }
}
