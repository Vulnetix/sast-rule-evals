// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-021: Sensitive data logged (password, token, secret, key)

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SensitiveLog {

    private static final Logger log = LoggerFactory.getLogger(SensitiveLog.class);

    public void authenticate(String username, String password) {
        // TRIGGERS: password logged at debug level
        log.debug("Login attempt: user={}, password={}", username, password);
    }

    public void callApi(String endpoint, String apikey) {
        // TRIGGERS: API key logged
        log.info("Calling {} with apikey={}", endpoint, apikey);
    }

    public void storeToken(String userId, String token) {
        // TRIGGERS: token logged
        log.warn("Token for user {}: token={}", userId, token);
    }

    public void rotateSecret(String oldSecret, String newSecret) {
        // TRIGGERS: secret logged
        log.error("Secret rotation failed: old secret={}", oldSecret);
    }
}
