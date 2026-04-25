// Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
// This file demonstrates VNX-CRYPTO-009: weak PRNG (rand/srand) in C

#include <stdlib.h>
#include <time.h>
#include <string.h>

void generate_session_token(char *token, size_t len) {
    // TRIGGERS VNX-CRYPTO-009: srand seeded with time - predictable seed
    srand((unsigned int)time(NULL));
    for (size_t i = 0; i < len; i++) {
        // TRIGGERS VNX-CRYPTO-009: rand() is not cryptographically secure
        token[i] = 'A' + (rand() % 26);
    }
    token[len] = '\0';
}

int generate_otp(void) {
    // TRIGGERS VNX-CRYPTO-009: rand() used for security-sensitive OTP
    return rand() % 1000000;
}

double roll_crypto_key(void) {
    // TRIGGERS VNX-CRYPTO-009: drand48 is not cryptographically secure
    return drand48();
}
