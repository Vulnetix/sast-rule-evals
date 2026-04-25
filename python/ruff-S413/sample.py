# Sample for Ruff rule S413: suspicious-pycrypto-import
# This file is designed to trigger the S413 rule.
# Run: ruff check --select S413 <this_file>

import Crypto.Random
