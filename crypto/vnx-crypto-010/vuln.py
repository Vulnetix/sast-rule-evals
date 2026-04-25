# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-CRYPTO-010: hardcoded IV/nonce in crypto operations

from Crypto.Cipher import AES
import binascii

KEY = b'sixteen byte key'

def encrypt_message_bad(plaintext: bytes) -> bytes:
    # TRIGGERS VNX-CRYPTO-010: hardcoded zero IV - reusing the same IV with same key
    iv = b'\x00' * 16
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return cipher.encrypt(plaintext)

def encrypt_gcm_bad(plaintext: bytes) -> bytes:
    # TRIGGERS VNX-CRYPTO-010: hardcoded nonce - catastrophic for GCM mode
    nonce = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    return cipher.encrypt(plaintext)

def hash_password_bad(password: str) -> str:
    # TRIGGERS VNX-CRYPTO-010: zero salt makes rainbow table attacks trivial
    salt = b'\x00' * 16
    import hashlib
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()
