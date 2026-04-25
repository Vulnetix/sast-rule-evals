# Sample for Ruff rule F524: string-dot-format-missing-arguments
# This file is designed to trigger the F524 rule.
# Run: ruff check --select F524 <this_file>

"{greeting}, {name}".format(name="World")
