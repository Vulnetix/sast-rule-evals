import asyncio


async def func():
    async with asyncio.timeout(2):
        do_something()

