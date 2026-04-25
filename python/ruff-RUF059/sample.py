# Sample for Ruff rule RUF059: unused-unpacked-variable
# This file is designed to trigger the RUF059 rule.
# Run: ruff check --select RUF059 <this_file>

def get_pair():
    return 1, 2


def foo():
    x, y = get_pair()
    return x
