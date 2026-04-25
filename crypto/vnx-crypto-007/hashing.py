# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-CRYPTO-007: Weak password hashing

import hashlib

def hash_password_md5(password):
    # VULNERABLE: MD5 is cryptographically broken for password storage
    return hashlib.md5(password.encode()).hexdigest()

def hash_password_sha1(password):
    # VULNERABLE: SHA-1 is deprecated for password hashing
    return hashlib.sha1(password.encode()).hexdigest()

def hash_password_sha256(password):
    # VULNERABLE: SHA-256 without salt or KDF is insufficient for passwords
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, stored_hash):
    # VULNERABLE: using SHA-1 for password verification
    computed = hashlib.sha1(password.encode()).hexdigest()
    return computed == stored_hash
