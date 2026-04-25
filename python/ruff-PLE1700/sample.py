# Sample for Ruff rule PLE1700: yield-from-in-async-function
# This file is designed to trigger the PLE1700 rule.
# Run: ruff check --select PLE1700 <this_file>

async def numbers():
    yield from [1, 2, 3, 4, 5]
