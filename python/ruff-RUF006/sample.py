# Sample for Ruff rule RUF006: asyncio-dangling-task
# This file is designed to trigger the RUF006 rule.
# Run: ruff check --select RUF006 <this_file>

import asyncio

async def main():
    asyncio.ensure_future(coro())  # RUF006: store task reference

