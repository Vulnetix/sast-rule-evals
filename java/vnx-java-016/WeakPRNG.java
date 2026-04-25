// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-JAVA-016: Weak PRNG (java.util.Random) for security values

import java.util.Random;

public class WeakPRNG {

    // TRIGGERS: new Random() used to generate security-sensitive values
    private static final Random RANDOM = new Random();

    public String generateSessionToken() {
        // VULNERABLE: predictable session token
        return String.valueOf(RANDOM.nextLong());
    }

    public String generateApiKey() {
        // VULNERABLE: Math.random() for API key generation
        long part1 = (long)(Math.random() * Long.MAX_VALUE);
        long part2 = (long)(Math.random() * Long.MAX_VALUE);
        return Long.toHexString(part1) + Long.toHexString(part2);
    }

    public int generateOtpCode() {
        // VULNERABLE: new Random() for OTP
        Random rng = new Random();
        return rng.nextInt(999999);
    }
}
