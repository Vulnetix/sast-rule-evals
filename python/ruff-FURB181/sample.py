# Sample for Ruff rule FURB181: hashlib-digest-hex
# This file is designed to trigger the FURB181 rule.
# Run: ruff check --select FURB181 <this_file>

from hashlib import sha512

hashed = sha512(b"some data").digest().hex()
