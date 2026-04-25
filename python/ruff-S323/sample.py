# Sample for Ruff rule S323: suspicious-unverified-context-usage
# This file is designed to trigger the S323 rule.
# Run: ruff check --select S323 <this_file>

import ssl
ctx = ssl._create_unverified_context()  # S323

