# Sample for Ruff rule PLE1132: repeated-keyword-argument
# This file is designed to trigger the PLE1132 rule.
# Run: ruff check --select PLE1132 <this_file>

func(1, 2, c=3, **{"c": 4})
