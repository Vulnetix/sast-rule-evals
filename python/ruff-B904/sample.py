# Sample for Ruff rule B904: raise-without-from-inside-except
# This file is designed to trigger the B904 rule.
# Run: ruff check --select B904 <this_file>

try:
    ...
except FileNotFoundError:
    if ...:
        raise RuntimeError("...")
    else:
        raise UserWarning("...")
