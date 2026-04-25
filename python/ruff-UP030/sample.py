# Sample for Ruff rule UP030: format-literals
# This file is designed to trigger the UP030 rule.
# Run: ruff check --select UP030 <this_file>

"{0}, {1}".format("Hello", "World")  # "Hello, World"
