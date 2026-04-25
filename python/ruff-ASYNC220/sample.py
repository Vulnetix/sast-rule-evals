# Sample for Ruff rule ASYNC220: create-subprocess-in-async-function
# This file is designed to trigger the ASYNC220 rule.
# Run: ruff check --select ASYNC220 <this_file>

import os


async def foo():
    os.popen(cmd)
