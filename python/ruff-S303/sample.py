# Sample for Ruff rule S303: suspicious-insecure-hash-usage
# This file is designed to trigger the S303 rule.
# Run: ruff check --select S303 <this_file>

import hashlib
h = hashlib.md5(b"data")  # S303: weak hash
h2 = hashlib.sha1(b"data")

