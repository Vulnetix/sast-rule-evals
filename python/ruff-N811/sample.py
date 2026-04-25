# Sample for Ruff rule N811: constant-imported-as-non-constant
# This file is designed to trigger the N811 rule.
# Run: ruff check --select N811 <this_file>

from os import getcwd as GETCWD  # N811: constant imported as non-constant

