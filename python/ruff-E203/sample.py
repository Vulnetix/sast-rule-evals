# Sample for Ruff rule E203: whitespace-before-punctuation
# This file is designed to trigger the E203 rule.
# Run: ruff check --select E203 <this_file>

if x == 4: print(x, y); x, y = y , x
