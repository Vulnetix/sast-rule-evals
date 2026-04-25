# Sample for Ruff rule TRY301: raise-within-try
# This file is designed to trigger the TRY301 rule.
# Run: ruff check --select TRY301 <this_file>

def bar():
    pass


def foo():
    try:
        a = bar()
        if not a:
            raise ValueError
    except ValueError:
        raise
