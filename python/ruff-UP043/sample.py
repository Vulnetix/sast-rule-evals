# Sample for Ruff rule UP043: unnecessary-default-type-args
# This file is designed to trigger the UP043 rule.
# Run: ruff check --select UP043 <this_file>

from collections.abc import Generator, AsyncGenerator


def sync_gen() -> Generator[int, None, None]:
    yield 42


async def async_gen() -> AsyncGenerator[int, None]:
    yield 42
