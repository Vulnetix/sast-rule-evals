# Sample for Ruff rule UP028: yield-in-for-loop
# This file is designed to trigger the UP028 rule.
# Run: ruff check --select UP028 <this_file>

def bar():
    for x in foo:
        yield x

    global y
    for y in foo:
        yield y
