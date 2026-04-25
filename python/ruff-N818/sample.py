# Sample for Ruff rule N818: error-suffix-on-exception-name
# This file is designed to trigger the N818 rule.
# Run: ruff check --select N818 <this_file>

class MyCustomError(Exception):  # N818: should end with Error
    pass

