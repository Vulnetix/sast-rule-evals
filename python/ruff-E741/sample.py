# Sample for Ruff rule E741: ambiguous-variable-name
# This file is designed to trigger the E741 rule.
# Run: ruff check --select E741 <this_file>

l = 1  # E741: ambiguous name
O = 2  # E741
I = 3  # E741
for l in range(10):  # E741
    pass

