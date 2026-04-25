# Sample for Ruff rule ASYNC115: async-zero-sleep
# This file is designed to trigger the ASYNC115 rule.
# Run: ruff check --select ASYNC115 <this_file>

import asyncio

async def tick():
    await asyncio.sleep(0)  # ASYNC115: no-op sleep

