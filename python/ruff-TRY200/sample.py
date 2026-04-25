# Sample for Ruff rule TRY200: reraise-no-cause
# This file is designed to trigger the TRY200 rule.
# Run: ruff check --select TRY200 <this_file>

def reciprocal(n):
    try:
        return 1 / n
    except ZeroDivisionError:
        raise ValueError()
