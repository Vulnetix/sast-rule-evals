# Sample for Ruff rule S305: suspicious-insecure-cipher-mode-usage
# This file is designed to trigger the S305 rule.
# Run: ruff check --select S305 <this_file>

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

algorithm = algorithms.ARC4(key)
cipher = Cipher(algorithm, mode=modes.ECB(iv))
encryptor = cipher.encryptor()
