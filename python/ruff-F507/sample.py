# Sample for Ruff rule F507: percent-format-positional-count-mismatch
# This file is designed to trigger the F507 rule.
# Run: ruff check --select F507 <this_file>

"%s, %s" % ("Hello", "world", "!")
