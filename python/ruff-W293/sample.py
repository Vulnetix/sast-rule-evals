# Sample for Ruff rule W293: blank-line-with-whitespace
# This file is designed to trigger the W293 rule.
# Run: ruff check --select W293 <this_file>

class Foo(object):\n    \n    bang = 12
