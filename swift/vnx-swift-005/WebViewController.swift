// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-SWIFT-005: WKWebView JavaScript auto-open-windows enabled

import UIKit
import WebKit

class WebViewController: UIViewController {
    // VULNERABLE: javaScriptCanOpenWindowsAutomatically = true
    func setupWebView() -> WKWebView {
        let preferences = WKPreferences()
        preferences.javaScriptCanOpenWindowsAutomatically = true

        let configuration = WKWebViewConfiguration()
        configuration.preferences = preferences

        return WKWebView(frame: .zero, configuration: configuration)
    }

    // VULNERABLE: Using deprecated UIWebView
    func createLegacyWebView() -> UIWebView {
        let webView = UIWebView(frame: view.bounds)
        return webView
    }
}
