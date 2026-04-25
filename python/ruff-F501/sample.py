# Sample for Ruff rule F501: percent-format-invalid-format
# This file is designed to trigger the F501 rule.
# Run: ruff check --select F501 <this_file>

"Hello, %" % "world"
