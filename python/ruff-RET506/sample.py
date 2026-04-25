# Sample for Ruff rule RET506: superfluous-else-raise
# This file is designed to trigger the RET506 rule.
# Run: ruff check --select RET506 <this_file>

def check(x):
    if x < 0:
        raise ValueError("negative")
    else:  # RET506: superfluous else after raise
        return x

