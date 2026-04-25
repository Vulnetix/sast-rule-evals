# Sample for Ruff rule N803: invalid-argument-name
# This file is designed to trigger the N803 rule.
# Run: ruff check --select N803 <this_file>

def process(Data, Items):  # N803: args should be lowercase
    pass

