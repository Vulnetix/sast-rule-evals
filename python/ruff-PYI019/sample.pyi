from typing import TypeVar

_Self = TypeVar("_Self")

class Foo:
    def copy(self: _Self) -> _Self: ...
