# Sample for Ruff rule FBT003: boolean-positional-value-in-call
# This file is designed to trigger the FBT003 rule.
# Run: ruff check --select FBT003 <this_file>

def process(data, verbose):
    pass

process("hello", True)  # FBT003: bool positional

