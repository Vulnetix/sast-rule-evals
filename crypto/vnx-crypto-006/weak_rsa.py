from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# VNX-CRYPTO-006: Weak RSA key size (1024 bits)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=1024,
    backend=default_backend()
)
