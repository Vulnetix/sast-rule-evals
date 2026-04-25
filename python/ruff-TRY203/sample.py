# Sample for Ruff rule TRY203: useless-try-except
# This file is designed to trigger the TRY203 rule.
# Run: ruff check --select TRY203 <this_file>

def foo():
    try:
        bar()
    except NotImplementedError:
        raise
