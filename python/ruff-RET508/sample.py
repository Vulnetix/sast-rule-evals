# Sample for Ruff rule RET508: superfluous-else-break
# This file is designed to trigger the RET508 rule.
# Run: ruff check --select RET508 <this_file>

def foo(bar, baz):
    for i in bar:
        if i > baz:
            break
        else:
            x = 0
