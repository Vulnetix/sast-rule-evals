# Sample for Ruff rule S505: weak-cryptographic-key
# This file is designed to trigger the S505 rule.
# Run: ruff check --select S505 <this_file>

from cryptography.hazmat.primitives.asymmetric import dsa, ec

dsa.generate_private_key(key_size=512)
ec.generate_private_key(curve=ec.SECT163K1())
