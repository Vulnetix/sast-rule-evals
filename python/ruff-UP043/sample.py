from collections.abc import Generator

def foo() -> Generator[int, None, None]:
    yield 1
