from typing import Unpack

def foo(*args: Unpack[tuple[int, ...]]) -> None:
    pass
