# Sample for Ruff rule PLE2502: bidirectional-unicode
# This file is designed to trigger the PLE2502 rule.
# Run: ruff check --select PLE2502 <this_file>

example = "x‏" * 100  #    "‏x" is assigned
