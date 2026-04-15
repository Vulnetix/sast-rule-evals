import hashlib

def hash_password(password):
    # VNX-CRYPTO-001: MD5 for hashing
    return hashlib.md5(password.encode()).hexdigest()
