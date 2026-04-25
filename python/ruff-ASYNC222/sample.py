# Sample for Ruff rule ASYNC222: wait-for-process-in-async-function
# This file is designed to trigger the ASYNC222 rule.
# Run: ruff check --select ASYNC222 <this_file>

import os


async def foo():
    os.waitpid(0)
