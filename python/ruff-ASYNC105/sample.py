# Sample for Ruff rule ASYNC105: trio-sync-call
# This file is designed to trigger the ASYNC105 rule.
# Run: ruff check --select ASYNC105 <this_file>

import trio


async def double_sleep(x):
    trio.sleep(2 * x)
