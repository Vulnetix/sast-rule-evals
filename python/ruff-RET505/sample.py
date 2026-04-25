# Sample for Ruff rule RET505: superfluous-else-return
# This file is designed to trigger the RET505 rule.
# Run: ruff check --select RET505 <this_file>

def check(x):
    if x > 0:
        return "positive"
    elif x < 0:  # RET505: superfluous elif after return
        return "negative"
    else:
        return "zero"

