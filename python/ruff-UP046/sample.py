from typing import Generic, TypeVar
T = TypeVar("T")
class Foo(Generic[T]):
    pass
