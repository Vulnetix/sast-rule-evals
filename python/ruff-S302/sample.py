# Sample for Ruff rule S302: suspicious-marshal-usage
# This file is designed to trigger the S302 rule.
# Run: ruff check --select S302 <this_file>

import marshal
data = marshal.loads(raw_bytes)  # S302: marshal

