# Sample for Ruff rule RUF072: useless-finally
# This file is designed to trigger the RUF072 rule.
# Run: ruff check --select RUF072 <this_file>

try:
    foo()
except Exception:
    bar()
finally:
    pass
