# Sample for Ruff rule PLR1708: stop-iteration-return
# This file is designed to trigger the PLR1708 rule.
# Run: ruff check --select PLR1708 <this_file>

def my_generator():
    yield 1
    yield 2
    raise StopIteration  # This causes RuntimeError at runtime
