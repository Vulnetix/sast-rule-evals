# Sample for Ruff rule ARG001: unused-function-argument
# This file is designed to trigger the ARG001 rule.
# Run: ruff check --select ARG001 <this_file>

def process(data, unused_param):  # ARG001
    return data

