# Sample for Ruff rule F634: if-tuple
# This file is designed to trigger the F634 rule.
# Run: ruff check --select F634 <this_file>

if (False,):
    print("This will always run")
