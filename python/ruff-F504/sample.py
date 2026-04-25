# Sample for Ruff rule F504: percent-format-extra-named-arguments
# This file is designed to trigger the F504 rule.
# Run: ruff check --select F504 <this_file>

"Hello, %(name)s" % {"greeting": "Hello", "name": "World"}
