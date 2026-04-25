# Sample for Ruff rule S105: hardcoded-password-string
# This file is designed to trigger the S105 rule.
# Run: ruff check --select S105 <this_file>

password = "hunter2"  # S105: hardcoded password
api_key = "secret123"

