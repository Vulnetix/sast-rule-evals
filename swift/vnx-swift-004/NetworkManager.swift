// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-SWIFT-004: TLS certificate validation disabled

import Foundation

class InsecureNetworkManager: NSObject, URLSessionDelegate {
    // VULNERABLE: URLCredential(trust:) bypasses certificate validation
    func urlSession(_ session: URLSession,
                    didReceive challenge: URLAuthenticationChallenge,
                    completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
        if challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodServerTrust {
            let credential = URLCredential(trust: challenge.protectionSpace.serverTrust!)
            completionHandler(.useCredential, credential)
        }
    }

    func makeRequest(to url: URL) {
        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config, delegate: self, delegateQueue: nil)
        session.dataTask(with: url) { data, _, _ in
            _ = data
        }.resume()
    }
}
