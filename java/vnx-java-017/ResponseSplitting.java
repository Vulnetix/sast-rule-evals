// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-017: HTTP response splitting via unsanitised header value

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class ResponseSplitting {

    public void handleRedirect(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // VULNERABLE: user input placed directly in Location header
        String url = request.getParameter("redirectUrl");
        response.addHeader("Location", url);  // attacker can inject \r\n
    }

    public void setCustomHeader(HttpServletRequest request, HttpServletResponse response) {
        // VULNERABLE: unsanitised query parameter in custom header
        String headerValue = request.getParameter("theme");
        response.setHeader("X-App-Theme", headerValue);
    }

    public void doRedirect(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // VULNERABLE: sendRedirect with raw user input allows CRLF injection
        String next = request.getParameter("next");
        response.sendRedirect(request.getContextPath() + next);
    }
}
