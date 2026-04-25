# Sample for Ruff rule T201: print
# This file is designed to trigger the T201 rule.
# Run: ruff check --select T201 <this_file>

def debug_info():
    print("debugging value:", x)  # T201: print found
    return x

