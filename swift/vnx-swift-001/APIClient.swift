// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-SWIFT-001: Hardcoded API key/secret in Swift source

import Foundation

class APIClient {
    // VULNERABLE: Hardcoded API key
    private let api_key: String = "AIzaSyD-abc123def456ghi789jkl012mno345"

    // VULNERABLE: Hardcoded client secret
    private let client_secret = "sk_live_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"

    // VULNERABLE: Hardcoded auth token
    var authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.hardcoded_payload"

    func sendRequest(endpoint: String) -> Data? {
        var request = URLRequest(url: URL(string: endpoint)!)
        request.setValue(api_key, forHTTPHeaderField: "X-API-Key")
        request.setValue("Bearer \(authToken)", forHTTPHeaderField: "Authorization")

        var result: Data?
        let semaphore = DispatchSemaphore(value: 0)
        URLSession.shared.dataTask(with: request) { data, _, _ in
            result = data
            semaphore.signal()
        }.resume()
        semaphore.wait()
        return result
    }
}
