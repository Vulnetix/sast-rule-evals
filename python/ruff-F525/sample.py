# Sample for Ruff rule F525: string-dot-format-mixing-automatic
# This file is designed to trigger the F525 rule.
# Run: ruff check --select F525 <this_file>

"{0}, {}".format("Hello", "World")
