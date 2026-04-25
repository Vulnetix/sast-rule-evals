# Sample for Ruff rule ASYNC250: blocking-input-in-async-function
# This file is designed to trigger the ASYNC250 rule.
# Run: ruff check --select ASYNC250 <this_file>

async def foo():
    username = input("Username:")
