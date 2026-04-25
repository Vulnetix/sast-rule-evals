# Sample for Ruff rule F521: string-dot-format-invalid-format
# This file is designed to trigger the F521 rule.
# Run: ruff check --select F521 <this_file>

"{".format(foo)
