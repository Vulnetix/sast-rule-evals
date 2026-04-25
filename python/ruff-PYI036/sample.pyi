from typing import NoReturn

class Foo:
    def __exit__(self, *args: NoReturn) -> None: ...
