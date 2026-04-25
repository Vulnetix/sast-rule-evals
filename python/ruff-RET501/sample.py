# Sample for Ruff rule RET501: unnecessary-return-none
# This file is designed to trigger the RET501 rule.
# Run: ruff check --select RET501 <this_file>

def get_value(bar):
    if not bar:
        return
    return None  # RET501: explicit None return when function only returns None
