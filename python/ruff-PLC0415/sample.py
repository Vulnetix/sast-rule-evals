# Sample for Ruff rule PLC0415: import-outside-top-level
# This file is designed to trigger the PLC0415 rule.
# Run: ruff check --select PLC0415 <this_file>

def initialize():
    import os  # PLC0415: non-toplevel import
    return os.getcwd()

