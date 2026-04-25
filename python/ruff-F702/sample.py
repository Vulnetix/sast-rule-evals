# Sample for Ruff rule F702: continue-outside-loop
# This file is designed to trigger the F702 rule.
# Run: ruff check --select F702 <this_file>

def foo():
    continue  # SyntaxError
