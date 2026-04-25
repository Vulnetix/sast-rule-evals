# Sample for Ruff rule C901: complex-structure
# This file is designed to trigger the C901 rule.
# Run: ruff check --select C901 <this_file>

def foo(a, b, c):
    if a:
        if b:
            if c:
                return 1
            else:
                return 2
        else:
            return 3
    else:
        return 4
