# Sample for Ruff rule RET507: superfluous-else-continue
# This file is designed to trigger the RET507 rule.
# Run: ruff check --select RET507 <this_file>

def foo(bar, baz):
    for i in bar:
        if i < baz:
            continue
        else:
            x = 0
