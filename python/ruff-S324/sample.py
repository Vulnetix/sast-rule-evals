# Sample for Ruff rule S324: hashlib-insecure-hash-function
# This file is designed to trigger the S324 rule.
# Run: ruff check --select S324 <this_file>

import hashlib
h = hashlib.md5(b"password")  # S324: weak hash

