# Sample for Ruff rule COM812: missing-trailing-comma
# This file is designed to trigger the COM812 rule.
# Run: ruff check --select COM812 <this_file>

x = (
    1,
    2,
    3  # COM812: trailing comma missing
)

