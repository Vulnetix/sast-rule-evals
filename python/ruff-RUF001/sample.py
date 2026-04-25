# Sample for Ruff rule RUF001: ambiguous-unicode-character-string
# This file is designed to trigger the RUF001 rule.
# Run: ruff check --select RUF001 <this_file>

msg = "Hеllo"  # RUF001: Cyrillic 'е' looks like Latin 'e'

