# Sample for Ruff rule S110: try-except-pass
# This file is designed to trigger the S110 rule.
# Run: ruff check --select S110 <this_file>

try:
    connect()
except Exception:
    pass  # S110: try-except-pass

