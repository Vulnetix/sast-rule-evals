# Sample for Ruff rule S311: suspicious-non-cryptographic-random-usage
# This file is designed to trigger the S311 rule.
# Run: ruff check --select S311 <this_file>

import random
token = random.randint(0, 1000000)  # S311: not cryptographic

