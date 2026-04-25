# Sample for Ruff rule PLR0915: too-many-statements
# This file is designed to trigger the PLR0915 rule.
# Run: ruff check --select PLR0915 <this_file>

def is_even(number: int) -> bool:
    if number == 0:
        return True
    elif number == 1:
        return False
    elif number == 2:
        return True
    elif number == 3:
        return False
    elif number == 4:
        return True
    elif number == 5:
        return False
    else:
        ...
