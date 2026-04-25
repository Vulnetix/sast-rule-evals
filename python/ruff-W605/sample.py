# Sample for Ruff rule W605: invalid-escape-sequence
# This file is designed to trigger the W605 rule.
# Run: ruff check --select W605 <this_file>

pattern = "\p"  # W605: invalid escape
other = "\d+"

