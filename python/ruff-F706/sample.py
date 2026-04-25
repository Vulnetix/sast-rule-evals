# Sample for Ruff rule F706: return-outside-function
# This file is designed to trigger the F706 rule.
# Run: ruff check --select F706 <this_file>

class Foo:
    return 1
