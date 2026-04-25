# Sample for Ruff rule FBT001: boolean-type-hint-positional-argument
# This file is designed to trigger the FBT001 rule.
# Run: ruff check --select FBT001 <this_file>

def process(data: str, verbose: bool):  # FBT001: bool arg
    if verbose:
        print(data)

