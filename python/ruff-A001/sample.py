# Sample for Ruff rule A001: builtin-variable-shadowing
# This file is designed to trigger the A001 rule.
# Run: ruff check --select A001 <this_file>

def find_max(list_of_lists):
    max = 0
    for flat_list in list_of_lists:
        for value in flat_list:
            max = max(max, value)  # TypeError: 'int' object is not callable
    return max
