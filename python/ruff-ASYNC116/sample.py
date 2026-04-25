# Sample for Ruff rule ASYNC116: long-sleep-not-forever
# This file is designed to trigger the ASYNC116 rule.
# Run: ruff check --select ASYNC116 <this_file>

import trio


async def func():
    await trio.sleep(86401)
