# Sample for Ruff rule FBT002: boolean-default-value-positional-argument
# This file is designed to trigger the FBT002 rule.
# Run: ruff check --select FBT002 <this_file>

def process(data, verbose=True):  # FBT002: bool default
    if verbose:
        print(data)

