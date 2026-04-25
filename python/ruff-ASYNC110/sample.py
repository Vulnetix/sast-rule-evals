# Sample for Ruff rule ASYNC110: async-busy-wait
# This file is designed to trigger the ASYNC110 rule.
# Run: ruff check --select ASYNC110 <this_file>

import asyncio

DONE = False


async def func():
    while not DONE:
        await asyncio.sleep(1)
