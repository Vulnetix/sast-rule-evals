# Sample for Ruff rule A004: builtin-import-shadowing
# This file is designed to trigger the A004 rule.
# Run: ruff check --select A004 <this_file>

from rich import print

print("Some message")
