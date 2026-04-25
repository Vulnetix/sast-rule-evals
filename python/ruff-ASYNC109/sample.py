# Sample for Ruff rule ASYNC109: async-function-with-timeout
# This file is designed to trigger the ASYNC109 rule.
# Run: ruff check --select ASYNC109 <this_file>

import asyncio

async def wait(timeout=None):  # ASYNC109: unused timeout arg
    await asyncio.sleep(1)

