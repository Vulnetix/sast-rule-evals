# Sample for Ruff rule RUF104: unmatched-suppression-comment
# This file is designed to trigger the RUF104 rule.
# Run: ruff check --select RUF104 <this_file>

def foo():
    # ruff: disable[E501]  # unmatched
    REALLY_LONG_VALUES = [...]

    print(REALLY_LONG_VALUES)
