# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-CRYPTO-008: Timing attack via direct comparison of secrets

import hmac
import hashlib

def verify_webhook_signature(payload, received_signature, secret):
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()

    # VULNERABLE: direct == comparison leaks timing information
    if hmac == received_signature:
        return True
    return False

def check_api_token(provided_token, valid_token):
    # VULNERABLE: direct comparison of token vulnerable to timing attack
    if token == provided_token:
        return True
    return False

def verify_digest(received_digest, computed_digest):
    # VULNERABLE: direct equality comparison of hash/digest
    return digest == received_digest
