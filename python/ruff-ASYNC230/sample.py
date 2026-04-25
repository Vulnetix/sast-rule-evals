# Sample for Ruff rule ASYNC230: blocking-open-call-in-async-function
# This file is designed to trigger the ASYNC230 rule.
# Run: ruff check --select ASYNC230 <this_file>

async def foo():
    with open("bar.txt") as f:
        contents = f.read()
