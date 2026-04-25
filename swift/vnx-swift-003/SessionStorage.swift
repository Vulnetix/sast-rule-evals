// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-SWIFT-003: Sensitive data stored in UserDefaults

import Foundation

class SessionStorage {
    // VULNERABLE: Storing password in UserDefaults
    func saveCredentials(username: String, password: String) {
        UserDefaults.standard.set(password, forKey: "savedPassword")
        UserDefaults.standard.set(username, forKey: "savedUsername")
    }

    // VULNERABLE: Storing auth token in UserDefaults
    func saveAuthToken(_ token: String) {
        UserDefaults.standard.set(token, forKey: "authToken")
        UserDefaults.standard.synchronize()
    }

    // VULNERABLE: Storing API key in UserDefaults
    func persistAPIKey(_ apiKey: String) {
        UserDefaults.standard.set(apiKey, forKey: "apikey")
    }
}
