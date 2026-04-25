import trio


async def long_running_task(timeout):
    ...


async def main():
    await long_running_task(timeout=2)

