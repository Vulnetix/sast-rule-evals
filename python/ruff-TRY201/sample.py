# Sample for Ruff rule TRY201: verbose-raise
# This file is designed to trigger the TRY201 rule.
# Run: ruff check --select TRY201 <this_file>

def foo():
    try:
        ...
    except ValueError as exc:
        raise exc
