# Sample for Ruff rule PLC1901: compare-to-empty-string
# This file is designed to trigger the PLC1901 rule.
# Run: ruff check --select PLC1901 <this_file>

s = ""
if s == "":  # PLC1901: compare to empty string
    pass

