from typing import Generic, TypeVar

T = TypeVar("T")

class Foo[U](Generic[T]):  # RUF053: mixed type params (PEP 695 syntax + Generic)
    pass
