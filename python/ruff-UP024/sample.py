# Sample for Ruff rule UP024: os-error-alias
# This file is designed to trigger the UP024 rule.
# Run: ruff check --select UP024 <this_file>

try:
    pass
except IOError:  # UP024: use OSError
    pass

