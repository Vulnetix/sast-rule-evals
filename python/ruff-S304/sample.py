# Sample for Ruff rule S304: suspicious-insecure-cipher-usage
# This file is designed to trigger the S304 rule.
# Run: ruff check --select S304 <this_file>

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

algorithm = algorithms.ARC4(key)
cipher = Cipher(algorithm, mode=None)
encryptor = cipher.encryptor()
