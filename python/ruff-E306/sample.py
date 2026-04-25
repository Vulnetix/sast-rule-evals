# Sample for Ruff rule E306: blank-lines-before-nested-definition
# This file is designed to trigger the E306 rule.
# Run: ruff check --select E306 <this_file>

def outer():
    def inner():
        pass
    def inner2():
        pass
