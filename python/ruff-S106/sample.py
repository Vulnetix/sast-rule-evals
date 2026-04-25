# Sample for Ruff rule S106: hardcoded-password-func-arg
# This file is designed to trigger the S106 rule.
# Run: ruff check --select S106 <this_file>

def connect(host, password="mysecret"):  # S106
    pass

