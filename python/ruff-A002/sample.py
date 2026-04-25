# Sample for Ruff rule A002: builtin-argument-shadowing
# This file is designed to trigger the A002 rule.
# Run: ruff check --select A002 <this_file>

def remove_duplicates(list, list2):
    result = set()
    for value in list:
        result.add(value)
    for value in list2:
        result.add(value)
    return list(result)  # TypeError: 'list' object is not callable
