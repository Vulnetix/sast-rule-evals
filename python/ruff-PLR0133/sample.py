# Sample for Ruff rule PLR0133: comparison-of-constant
# This file is designed to trigger the PLR0133 rule.
# Run: ruff check --select PLR0133 <this_file>

if 1 == 1:  # PLR0133: constant comparison
    pass

