import hashlib

def hash_data(data):
    # VNX-CRYPTO-002: SHA-1 for hashing
    return hashlib.sha1(data.encode()).hexdigest()
