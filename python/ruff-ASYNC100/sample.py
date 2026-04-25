# Sample for Ruff rule ASYNC100: cancel-scope-no-checkpoint
# This file is designed to trigger the ASYNC100 rule.
# Run: ruff check --select ASYNC100 <this_file>

import asyncio, time

async def slow_task():
    time.sleep(1)  # ASYNC100: blocking sleep in async

