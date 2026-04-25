# Sample for Ruff rule F523: string-dot-format-extra-positional-arguments
# This file is designed to trigger the F523 rule.
# Run: ruff check --select F523 <this_file>

"Hello, {0}".format("world", "!")
