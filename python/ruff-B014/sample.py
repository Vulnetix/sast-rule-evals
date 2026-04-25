# Sample for Ruff rule B014: duplicate-handler-exception
# This file is designed to trigger the B014 rule.
# Run: ruff check --select B014 <this_file>

try:
    pass
except (ValueError, Exception):  # B014: redundant exceptions
    pass

