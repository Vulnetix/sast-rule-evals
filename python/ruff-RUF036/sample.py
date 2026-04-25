# Sample for Ruff rule RUF036: none-not-at-end-of-union
# This file is designed to trigger the RUF036 rule.
# Run: ruff check --select RUF036 <this_file>

def func(arg: None | int): ...
