# Sample for Ruff rule B025: duplicate-try-block-exception
# This file is designed to trigger the B025 rule.
# Run: ruff check --select B025 <this_file>

try:
    risky()
except (ValueError, ValueError):  # B025: duplicate exception types
    pass

