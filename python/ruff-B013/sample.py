# Sample for Ruff rule B013: redundant-tuple-in-exception-handler
# This file is designed to trigger the B013 rule.
# Run: ruff check --select B013 <this_file>

try:
    pass
except (ValueError,):  # B013: redundant tuple
    pass

