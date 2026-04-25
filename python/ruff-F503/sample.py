# Sample for Ruff rule F503: percent-format-expected-sequence
# This file is designed to trigger the F503 rule.
# Run: ruff check --select F503 <this_file>

"%s, %s" % {"greeting": "Hello", "name": "World"}
