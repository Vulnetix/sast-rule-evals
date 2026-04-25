# Sample for Ruff rule RET503: implicit-return
# This file is designed to trigger the RET503 rule.
# Run: ruff check --select RET503 <this_file>

def foo(bar):
    if not bar:
        return 1
