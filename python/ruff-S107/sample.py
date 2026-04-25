# Sample for Ruff rule S107: hardcoded-password-default
# This file is designed to trigger the S107 rule.
# Run: ruff check --select S107 <this_file>

def connect_to_server(password="hunter2"): ...
