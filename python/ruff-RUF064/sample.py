# Sample for Ruff rule RUF064: non-octal-permissions
# This file is designed to trigger the RUF064 rule.
# Run: ruff check --select RUF064 <this_file>

os.chmod("foo", 644)
