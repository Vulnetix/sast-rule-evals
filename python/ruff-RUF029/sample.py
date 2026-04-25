# Sample for Ruff rule RUF029: unused-async
# This file is designed to trigger the RUF029 rule.
# Run: ruff check --select RUF029 <this_file>

async def foo():
    bar()
