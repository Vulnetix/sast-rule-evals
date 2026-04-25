# Sample for Ruff rule PLE0115: nonlocal-and-global
# This file is designed to trigger the PLE0115 rule.
# Run: ruff check --select PLE0115 <this_file>

counter = 0


def increment():
    global counter
    nonlocal counter
    counter += 1
