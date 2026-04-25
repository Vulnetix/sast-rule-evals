# Sample for Ruff rule E722: bare-except
# This file is designed to trigger the E722 rule.
# Run: ruff check --select E722 <this_file>

try:
    risky()
except:  # E722: bare except
    pass

