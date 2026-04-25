# Sample for Ruff rule PLR1701: repeated-isinstance-calls
# This file is designed to trigger the PLR1701 rule.
# Run: ruff check --select PLR1701 <this_file>

if isinstance(x, int) or isinstance(x, float):  # PLR1701: merge
    pass

