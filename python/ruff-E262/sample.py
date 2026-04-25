# Sample for Ruff rule E262: no-space-after-inline-comment
# This file is designed to trigger the E262 rule.
# Run: ruff check --select E262 <this_file>

x = x + 1  #Increment x
x = x + 1  #  Increment x
x = x + 1  # \xa0Increment x
