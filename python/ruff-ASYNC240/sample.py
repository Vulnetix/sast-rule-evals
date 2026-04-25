# Sample for Ruff rule ASYNC240: blocking-path-method-in-async-function
# This file is designed to trigger the ASYNC240 rule.
# Run: ruff check --select ASYNC240 <this_file>

import os


async def func():
    path = "my_file.txt"
    file_exists = os.path.exists(path)
