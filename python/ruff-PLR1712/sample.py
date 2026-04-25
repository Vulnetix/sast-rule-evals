# Sample for Ruff rule PLR1712: swap-with-temporary-variable
# This file is designed to trigger the PLR1712 rule.
# Run: ruff check --select PLR1712 <this_file>

def function(x, y):
    if x > y:
        temp = x
        x = y
        y = temp
    assert x <= y
