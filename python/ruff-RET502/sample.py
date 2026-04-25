# Sample for Ruff rule RET502: implicit-return-value
# This file is designed to trigger the RET502 rule.
# Run: ruff check --select RET502 <this_file>

def foo(bar):
    if not bar:
        return
    return 1
