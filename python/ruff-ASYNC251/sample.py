# Sample for Ruff rule ASYNC251: blocking-sleep-in-async-function
# This file is designed to trigger the ASYNC251 rule.
# Run: ruff check --select ASYNC251 <this_file>

import time


async def fetch():
    time.sleep(1)
