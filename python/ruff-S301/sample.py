# Sample for Ruff rule S301: suspicious-pickle-usage
# This file is designed to trigger the S301 rule.
# Run: ruff check --select S301 <this_file>

import pickle
data = pickle.loads(raw_bytes)  # S301: pickle

