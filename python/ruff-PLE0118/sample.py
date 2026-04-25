# Sample for Ruff rule PLE0118: load-before-global-declaration
# This file is designed to trigger the PLE0118 rule.
# Run: ruff check --select PLE0118 <this_file>

counter = 1


def increment():
    print(f"Adding 1 to {counter}")
    global counter
    counter += 1
